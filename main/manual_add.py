def manual_movie_add():
    user_movie_input = input('\nTitle,Year,Director OR ,Year,Director OR ,,Director etc.\n >> ').split(',', maxsplit=2)
    sanitized_movie_input = [element.lstrip() for element in user_movie_input]
    while len(sanitized_movie_input) < 3:
        sanitized_movie_input.append('')
    # TODO **
    test = {'title': sanitized_movie_input[0], 'year': sanitized_movie_input[1],
            'director(s)': sanitized_movie_input[2]}
    return test


if __name__ == '__main__':
    from main import csv_worker
    add_dict = manual_movie_add()
    csv_worker.csv_writer(add_dict)


# 1. ['Star Wars: The Clone Wars', '(2008–2020)', '']
