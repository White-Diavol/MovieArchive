# TODO - replace all text input with a GUI

# funcs = {
#     "add": ['1', '1.', 'add', 'add a movie', 'manual', 'manually', 'movie_add'],
#     "view": ['2', '2.', 'browse', 'browse the archive', 'archive', 'archv', 'archive_browse'],
#     "search": ['3', '3.', 'search', 'search for a movie', 'srch', 'online', 'imdb']
# }

affirmative = ['yes', 'y', 'yeah', 'yup']

run = input(
    'What do you want to do?\n\n\t1.Add or remove a movie\n\t2.Browse the local archives\n\t3.Search for a movie online\n\n>>Your choice: ').lower()

if run == '1':

    def movie_add():

        from main.manual_add import manual_movie_add

        if input('Do you wish to view the instructions y/n? ') in affirmative:
            print(
                'Please enter the details in this order:\n\n\tTitle,Year,Director(s)\nAll separated by commas, if you are missing ')
            manual_movie_add()
        else:
            manual_movie_add()

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
