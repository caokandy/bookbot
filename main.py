import sys
from stats import get_num_words
from stats import get_char_count
from stats import sorted_list

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    char_counts = get_char_count(text)
    sorted_counts = sorted_list(char_counts)

    print("============ BOOKBOT ============\nAnalyzing book found at books/...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_counts:
        if item["char"].isalpha():
    	    print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()


