# TODO - replace all text input with a GUI


class Runner:

    def __init__(self):
        self.affirmative = ['yes', 'y', 'yeah', 'yup']
        self.run = input(
            'What do you want to do?\n\n\t1.Add or remove a movie\n\t2.Browse the local archives\n\t3.Search for a '
            'movie online\n\n>>Your choice: ')

    def run_logic(self):

        if self.run == '1':

            from main.manual_add import manual_movie_add

            if input('Do you wish to view the instructions y/n? ') in self.affirmative:
                print(
                    'Please enter the details in this order:\n\n\tTitle,Year,Director(s)\nAll separated by commas, '
                    'if you are missing a velue enter a space instead')
                manual_movie_add()
            else:
                manual_movie_add()

        elif self.run == '2':
            from main.search_archive import search_input_handler

            search_input_handler()

        elif self.run == '3':
            import main.imdb_crawl as imdb_crawl

            request = imdb_crawl.test_request(input('Please enter the movie title you are searching for: '))

            result = imdb_crawl.imdb_search(request_result=request)

            # TODO **
            input('Do you want to: \n\t1. Save this this to the archive\n\t2. Re-do the search?\n')
            if result:
                imdb_crawl.dict_to_csv(result)

        else:
            print('Unrecognized input try with 1, 2 or 3')


if __name__ == '__main__':
    main_runner = Runner()
    main_runner.run_logic()
