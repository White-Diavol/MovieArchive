import csv


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
        # TODO make a script to confirm the status
        print('Network code returned an error')


def imdb_search(movie_title, input_num=0):
    import re
    from bs4 import BeautifulSoup

    titles = []

    search_results = request(movie_title)

    soup_html = BeautifulSoup(search_results.text, 'html.parser')

    soup_results = soup_html.select('.lister-item.mode-advanced')

    if soup_results:
        for count, result in enumerate(soup_results, start=1):
            if count > 25:
                break
            actual_title = result.select('.lister-item-header > a')[0].text
            # year = result.select('h3 > span:nth-child(3)')[0].text

            if year := result.select('h3 > span:nth-child(3)'):
                year = year[0].text
            else:
                year = ''

            if description := result.select('div > p.text-muted:nth-of-type(2)'):
                description = description[0].text.rstrip()
                if description == '\nAdd a Plot':
                    description = ''
            else:
                description = ''

            print('\n', str(count) + ". " + actual_title + ',', year, description)
            titles.append(actual_title)

        # TODO - write a better handler for input here

        if input_num:
            title_user_index = input_num
        else:
            title_user_index = input('\n\nPlease enter a number corresponding to your requested title')

        while int(title_user_index) not in list(range(1, 26)):
            title_user_index = int(input('\nPlease enter a number corresponding to your requested title'))

        title_list_index = int(title_user_index) - 1

        # print(titles[title_list_index])

        search_year = \
            soup_html.select(f'.lister-item.mode-advanced:nth-child({title_user_index}) h3 > span:nth-child(3)')[
                0].text
        if search_year:
            search_year = re.search('\d{4}', search_year).group()
        else:
            search_year = "_"

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
            directors = "_"
        elif len(directors) == 1:
            directors = directors[0]
        elif len(directors) > 1:
            directors = " ".join(directors)
        # print(directors)

        return_dict = {'title': titles[title_list_index], 'year': search_year, "director(s)": directors}
        print('\n', return_dict)
        return return_dict
    else:
        print('No movie found with that title')


def dict_to_csv(dictionary):
    with open("Results/test_results.csv", "w") as results:
        writer = csv.DictWriter(results, fieldnames=['title', 'year', 'director(s)'])
        writer.writeheader()

        # TODO -  AttributeError: 'str' object has no attribute 'keys' wrong_fields = rowdict.keys() - self.fieldnames
        for result_list in dictionary:
            writer.writerow(result_list)


if __name__ == '__main__':
    output_list = [movie for number in list(range(1, 11)) if
                   (movie := imdb_search(movie_title='The Matrix', input_num=number)) is not None]

    if output_list:
        dict_to_csv(output_list)
