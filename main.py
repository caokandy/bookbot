from stats import get_num_words
from stats import get_char_count

def get_book_text(i):
    with open(i) as f:
        file_contents = f.read()
    return file_contents


def main():
    file_path = "/home/caoan/bookbot/bookbot/books/frankenstein.txt"
    text = get_book_text(file_path)
    total = get_char_count(text)
    print(f"{total} words found in the document")

main()

