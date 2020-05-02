def manual_movie_add():
    user_movie_input = input('\nTitle,Year,Director OR ,Year,Director OR ,,Director etc.\n >> ').split(',', maxsplit=2)
    sanitized_movie_input = [element.lstrip() for element in user_movie_input]
    while len(sanitized_movie_input) < 3:
        sanitized_movie_input.append('_')
    # TODO **
    test = {'Title': sanitized_movie_input[0], 'Year': sanitized_movie_input[1], 'Director': sanitized_movie_input[2]}
    # with open('Results/')
    # test.items()


if __name__ == '__main__':
    # while True:
    manual_movie_add()
