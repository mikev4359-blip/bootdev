def get_book_text(path_to_file: str):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words():
    text = get_book_text("books/frankenstein.txt")

    words = len(text.split())
    print(f"Found {words} total words")
