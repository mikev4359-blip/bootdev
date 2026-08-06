from stats import count_words, create_dict, chars_dict_to_sorted_list

def get_book_text(path_to_file: str):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def print_report(book_path, word_count, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"--------- Character Count -------")
    for letters in sorted_list:
        if letters[0].isalpha():
            print(f"{letters [0]}: {letters[1]}")
            continue
    print("============= END ===============")


book_link = "books/frankenstein.txt..."
book_contents = get_book_text("books/frankenstein.txt")
count = count_words(book_contents)
letter_counts = create_dict(book_contents)
sorted_list = chars_dict_to_sorted_list(letter_counts)

print_report(book_link, count, sorted_list)