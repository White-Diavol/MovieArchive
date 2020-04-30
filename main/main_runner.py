# TODO - replace all text input with a GUI

funcs = {
    "add": ['1', '1.', 'add', 'add a movie', 'manual', 'manually', 'movie_add'],
    "view": ['2', '2.', 'browse', 'browse the archive', 'archive', 'archv', 'archive_browse'],
    "search": ['3', '3.', 'search', 'search for a movie', 'srch', 'online', 'imdb']
}

affirmative = ['yes', 'y', 'yeah', 'yup', 'sure']

run = input(
    'What do you want to do?\n\n\t1.Add a movie manually\n\t2.Browse the local archives\n\t3.Search for a movie online\n\n>>Your choice: ').lower()

if run == '1':

    def movie_add():
        if input('Do you wish to view the instructions y/n? ') in affirmative:
            print('name=The Matrix, director=Wachowskis, year=1994')


    movie_add()

elif run == '2':
    from main.search_archive import search_input_handler


    def archive_browse():
        search_input_handler()


    archive_browse()

elif run == '3':
    from main.imdb_crawl import dict_to_csv, imdb_search


    def online_search():
        result = imdb_search(input('Please enter the movie title you are searching for: '))
        if result:
            dict_to_csv(result)


    online_search()

else:
    print('Unrecognized input try with 1, 2 or 3')
