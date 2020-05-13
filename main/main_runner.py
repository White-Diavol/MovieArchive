# TODO - replace all text input with a GUI


class Runner:

    def __init__(self):
        self.affirmative = ['yes', 'y', 'yeah', 'yup']
        self.run = input(
            'What do you want to do?\n\n\t1.Add a movie\n\t2.Remove a movie\n\t3.Browse the local '
            'archives\n\t3.Search for a '
            'movie online\n\n>>Your choice: ')

    def run_logic(self):

        if self.run == '1':

            from main.manual_add import manual_movie_add
            from main.csv_worker import csv_writer

            if input('Do you wish to view the instructions y/n? ') in self.affirmative:
                print(
                    'Please enter the details in this order:\n\n\tTitle,Year,Director(s)\nAll separated by commas, '
                    'if you are missing a velue enter a space instead')
                movie = manual_movie_add()
                csv_writer(movie)
            else:
                movie = manual_movie_add()
                csv_writer(movie)

        elif self.run == '2':
            from main.search_archive import search_input_handler

            to_remove = search_input_handler(print_out=False)
            print('The following was found with those parameters: \n')
            for count, movie in enumerate(to_remove, start=1):
                print(str(count) + ".", str(movie) + '\n')
            remove_input = input('Input title index that you wish to remove (1,2,3,4...) or q to quit >>')

            try:
                int(remove_input)
            except ValueError:
                if remove_input.lower() in ['q', 'quit']:
                    # TODO - Enable quitting
                    pass
                else:
                    print('Invalid input')

            else:
                remove_value = int(remove_input)
                if remove_value in range(1, 5):
                    remove_array_value_int = remove_value - 1

            pass

        elif self.run == '3':
            from main.search_archive import search_input_handler

            search_input_handler()

        elif self.run == '4':
            import main.imdb_crawl as imdb_crawl
            from main.csv_worker import csv_writer

            request = imdb_crawl.test_request(input('Please enter the movie title you are searching for: '))

            result = imdb_crawl.imdb_search(request_result=request)

            # TODO **
            input('Do you want to: \n\t1. Save this this to the archive\n\t2. Re-do the search?\n')
            if result:
                csv_writer(result)

        else:
            print('Unrecognized input try with 1, 2 or 3')


if __name__ == '__main__':
    main_runner = Runner()
    main_runner.run_logic()
