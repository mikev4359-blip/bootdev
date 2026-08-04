from stats import count_words, create_dict

def get_book_text(path_to_file: str):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

book_contents = get_book_text("books/frankenstein.txt")
count = count_words(book_contents)
letter_counts = create_dict(book_contents)
print(f"Found {count} total words")
print(dict)