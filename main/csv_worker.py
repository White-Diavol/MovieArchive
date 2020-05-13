import csv
import os


# TODO - Write a file handler here for both funcs

def csv_writer(movie_dict):
    movie_dict['year'] = str(movie_dict['year']).replace('–', '-')
    if os.path.exists('Results/test_results.csv'):
        archive_file_exists = True
    else:
        archive_file_exists = False
    with open("Results/test_results.csv", "a+", newline='') as results:
        writer = csv.DictWriter(results, fieldnames=['title', 'year', 'director(s)'])
        if not archive_file_exists:
            writer.writeheader()

        writer.writerow(
            {'title': movie_dict['title'], 'year': movie_dict['year'], 'director(s)': movie_dict['director(s)']})


def csv_reader(search_input=3, value='', print_out=True):
    """
    0 = Title
    1 = Year
    2 = Director(s)
    3 = All
    :int search_input:
    :string value:
    :return dict_list:
    """

    dict_list = []

    import os
    if not os.path.exists('Results/test_results.csv'):
        # TODO - add a way to communicate with the caller or complete a request
        print('The local archive does not exist, would you like to add a movie or browse for it online?')
        return 'something'
    else:
        import csv
        with open('Results/test_results.csv', 'r+') as movie_archive:

            csv_reader_obj = csv.reader(movie_archive)
            # print(search_input)
            if search_input == 3:
                for count, line in enumerate(csv_reader_obj):
                    if count == 0:
                        keys = line
                    else:
                        return_dict = dict(zip(keys, line))
                        if print_out:
                            print(str(count) + ".", return_dict)
                        dict_list.append(return_dict)

            else:
                for count, line in enumerate(csv_reader_obj):
                    if count == 0:
                        keys = line
                    elif value.lower() in line[search_input].lower():
                        if print_out:
                            print(str(count) + ".", line)
                        dict_list.append(dict(zip(keys, line)))

            return dict_list


# TODO - Make sure that a value doesn't exist in the program already
def csv_value_checker():
    pass

