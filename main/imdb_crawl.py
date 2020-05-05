def request(movie_title=''):
    import requests

    split_movie_title = movie_title.split(" ")
    query_movie_title = '+'.join(split_movie_title)

    search_results = requests.get(f"https://www.imdb.com/search/title/?title={query_movie_title}", headers={
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 '
                      'Firefox/75.0',
        'Accept-Language': 'en-US,en;q=0.5'})

    if search_results.status_code == 200:
        return search_results
    else:
        # TODO - check out connection and other issues
        print('Network code returned an error')


def imdb_search(request_result, input_num=0):
    import re
    from bs4 import BeautifulSoup

    titles = []
    year = []

    # search_results = request(movie_title)

    soup_html = BeautifulSoup(request_result.text, 'html.parser')

    soup_results = soup_html.select('.lister-item.mode-advanced')[:25]

    if soup_results:
        for count, result in enumerate(soup_results, start=1):

            actual_title = result.select('.lister-item-header > a')[0].text

            if actual_year := result.select('h3 > span:nth-child(3)'):
                actual_year = actual_year[0].text
            else:
                actual_year = ''

            if description := result.select('div > p.text-muted:nth-of-type(2)'):
                description = description[0].text.rstrip()
                if description == '\nAdd a Plot':
                    description = ''
            else:
                description = ''

            print('\n', str(count) + ". " + actual_title + ',', actual_year, description)
            titles.append(actual_title)
            year.append(actual_year)

        # TODO - write a better handler for input here

        if input_num:
            title_user_index = input_num
        else:
            title_user_index = input('\n\nPlease enter a number corresponding to your requested title: ')

        while int(title_user_index) not in list(range(1, 26)):
            title_user_index = int(input('\nPlease enter a number corresponding to your requested title: '))

        search_list_index = int(title_user_index) - 1

        # print(titles[title_list_index])

        directors = []

        content_html_string = str \
            (soup_html.select(f'.lister-item.mode-advanced:nth-child({title_user_index}) > div.lister-item-content')
             [0].prettify()).replace('\n', '')

        directors_regex = re.search("Director.?:.+?ghost", str(content_html_string))
        if directors_regex:
            directors_regex = directors_regex.group()
            directors_regex = re.findall("\">.+?</a>", directors_regex)

            for director in directors_regex:
                director = director.lstrip("\">")
                director = director.lstrip()
                director = director.rstrip("</a>")
                director = director.rstrip()
                directors.append(director)

        if len(directors) == 0:
            directors = ""
        elif len(directors) == 1:
            directors = directors[0]
        elif len(directors) > 1:
            directors = ",".join(directors)

        return_dict = {'title': titles[search_list_index], 'year': year[search_list_index], "director(s)": directors}
        print('\n', return_dict)
        return return_dict
    else:
        return None


if __name__ == '__main__':
    from main import csv_worker
    test_request = request('Star Wars')
    output_list = [movie for number in list(range(1, 26)) if
                   (movie := imdb_search(request_result=test_request, input_num=number)) is not None]

    if output_list:
        for dictionary in output_list:
            csv_worker.csv_writer(dictionary)
