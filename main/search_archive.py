import os


def csv_reader(search_input):
    if not os.path.exists('Results/test_results.csv'):
        # TODO - add a way to communicate with the caller
        print('The local archive does not exist, would you like to add a movie or browse for it online?')
        return 'something'
    else:
        import csv

        with open('Results/test_results.csv', 'r+') as movie_archive:

            csv_reader = csv.reader(movie_archive)
            for count, line in enumerate(csv_reader):
                if count == 0:
                    keys = line
                else:
                    print(dict(zip(keys, line)))
