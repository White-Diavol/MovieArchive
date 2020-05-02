def search_input_handler():
    # options = ['title', 'year', 'director', None]

    search_input = input(
        'Please enter the option number\n\n\t1. Title\n\t2. Year\n\t3. Director\n\t4. Display all results\n\n>> Your '
        'choice: ')

    try:
        int(search_input)
    except ValueError:
        if search_input.lower() in ['q', 'quit']:
            pass
        else:
            print('Invalid input')
    else:
        search_value = int(search_input)
        if search_value in range(1, 5):
            search_array_value_int = search_value - 1
            input_search_value = input('Enter the value you are looking for')
            csv_reader(search_array_value_int, input_search_value)
        else:
            print('Please enter a valid number')


def csv_reader(search_input=0, value=''):
    import os
    if not os.path.exists('Results/test_results.csv'):
        # TODO - add a way to communicate with the caller
        print('The local archive does not exist, would you like to add a movie or browse for it online?')
        return 'something'
    else:
        import csv
        with open('Results/test_results.csv', 'r+') as movie_archive:

            csv_reader_obj = csv.reader(movie_archive)

            if search_input == 4:
                for count, line in enumerate(csv_reader_obj):
                    if count == 0:
                        keys = line
                    else:
                        print(str(count) + ".", dict(zip(keys, line)))

            else:
                for count, line in enumerate(csv_reader_obj):
                    if count == 0:
                        pass
                    elif value in line[search_input].lower():
                        print(str(count) + ".", line)


if __name__ == '__main__':
    search_input_handler()
