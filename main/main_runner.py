from UdemyMovieArchive import imdb_crawl

funcs = {
    "add": ['1', '1.', 'add', 'add a movie', 'manual', 'manually', 'movie_add'],
    "view": ['2', '2.', 'browse', 'browse the archive', 'archive', 'archv', 'archive_browse'],
    "search": ['3', '3.', 'search', 'search for a movie', 'srch', 'online', 'imdb']
}

affirmative = ['yes', 'y', 'yeah', 'yup', 'sure']

run = input(
    'What do you want to do?\n1.Add a movie manually\n2.Browse the archives\n3.Search for a movie online\n\nYour choice: ')

for function in funcs:
    if run in function:
        pass

if run in funcs['add']:

    def movie_add():
        if input('Do you wish to view the instructions y/n? ') in affirmative:
            # print('First option is to input the information in the following order, leaving out any deatils you '
            #       'don\'t have')
            # print('')
            print('name=The Matrix, director=Wachowskis, year=1994')


    movie_add()

elif run in funcs['view']:

    def archive_browse():
        print('view the archive')


    archive_browse()


elif run in funcs['search']:

    def search_archive():

        result = imdb_crawl.imdb_search(input('Please enter the movie title you are searching for: '))
        if result:
            imdb_crawl.dict_to_csv(result)


    search_archive()

else:
    print('Unrecognized input try with 1, 2 or 3')
