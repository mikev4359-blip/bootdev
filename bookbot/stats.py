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