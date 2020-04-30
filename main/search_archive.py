def search_input_handler():
    search_input = input(
        'Please enter the option number\n\n\t1. Title\n\t2. Year\n\t3. Director\n\t4. Display all results\n\n>> Your choice: ').lower()

    if search_input == '1':
        title = input('Please enter the movie title: ')
        csv_reader(1, value=title)
    elif search_input == '2':
        year = input('Please enter the year: ')
        csv_reader(2, value=year)
    elif search_input == '3':
        director = input('Please enter the director: ')
        csv_reader(3, )
    elif search_input == '4':
        csv_reader(4)
    elif search_input == 'q':
        pass
    else:
        print(
            'No such input please choose a value and enter only the singular digit next to the given option: 1,2,3,4 or q to quit')
        search_input_handler()


def csv_reader(search_input, value=''):
    """
    :int search_input:
    :str value:
    :return:
    """
    import os
    if not os.path.exists('Results/test_results.csv'):
        # TODO - add a way to communicate with the caller
        print('The local archive does not exist, would you like to add a movie or browse for it online?')
        return 'something'
    else:
        import csv
        with open('Results/test_results.csv', 'r+') as movie_archive:
            csv_reader = csv.reader(movie_archive)

            if search_input == 1:
                for count, line in enumerate(csv_reader):
                    if count == 0:
                        keys = line
                    elif value in line[0].lower():
                        print(line)

            elif search_input == 2:
                for count, line in enumerate(csv_reader):
                    if count == 0:
                        keys = line
                    elif value in line[1].lower():
                        print(line)

            elif search_input == 3:
                for count, line in enumerate(csv_reader):
                    if count == 0:
                        keys = line
                    elif value in line[2].lower():
                        print(line)

            elif search_input == 4:
                for count, line in enumerate(csv_reader):
                    if count == 0:
                        keys = line
                    else:
                        print(dict(zip(keys, line)))


if __name__ == '__main__':
    search_input_handler()
