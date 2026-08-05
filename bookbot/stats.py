def get_book_text(path_to_file: str):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(book: str):

    words = len(book.split())

    return words

def create_dict(book: str):
    lowercase = book.lower()
    full_dict = {}

    for letter in lowercase:
        if letter in full_dict:
            full_dict[letter] += 1
        else:
            full_dict[letter] = 1

    return full_dict

def sort_on(a_tuple: tuple[str, int]):
    value_count = 0


    return a_tuple[1]

def chars_dict_to_sorted_list(some_dictionary):
    converted_list = []
    sorted_converted_list = []
    adding_tuple = ()

    for key in some_dictionary:
        adding_tuple = (key, some_dictionary[key])
        converted_list.append(adding_tuple)

    sorted_converted_list = sorted(converted_list, reverse=True, key=sort_on)
    return sorted_converted_list