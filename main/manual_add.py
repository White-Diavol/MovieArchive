def manual_movie_add():
    test = input('Title,Year,Director OR ,Year,Director OR ,,Director etc.\n >> ').split(',', maxsplit=2)
    output_list = [element.lstrip() for element in test]
    print(output_list)


if __name__ == '__main__':
    manual_movie_add()
