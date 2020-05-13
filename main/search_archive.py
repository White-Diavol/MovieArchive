
def search_input_handler(print_out=True):
    from main.csv_worker import csv_reader
    options = ['title', 'year', 'director']

    search_input = input(
        'Please enter the option number\n\n\t1. Title\n\t2. Year\n\t3. Director\n\t4. Display all results\n\n>> Your '
        'choice: ')

    try:
        int(search_input)
    except ValueError:
        if search_input.lower() in ['q', 'quit']:
            # TODO - Enable quitting
            pass
        else:
            print('Invalid input')
    else:
        search_value = int(search_input)
        if search_value in range(1, 5):
            search_array_value_int = search_value - 1

            if search_value == 4:
                input_search_value = None
            else:
                input_search_value = input(f'Enter the {options[search_array_value_int]} you are looking for: ')

            return csv_reader(search_array_value_int, input_search_value, print_out=print_out)

        else:
            print('Please enter a valid number')


if __name__ == '__main__':
    search_input_handler()
