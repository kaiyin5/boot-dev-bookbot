from stats import get_num_words, get_num_chars, get_char_num_pair
import sys

def main():
    # handling user argument
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    

    # getting data
    try:
        book_text = get_book_text(file_path)
    except FileNotFoundError as e:
        print(e)
        sys.exit(2)
    num_words = get_num_words(book_text)
    num_chars = get_num_chars(book_text)
    char_num_pair = get_char_num_pair(num_chars)

    # printing report
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for pair in char_num_pair:
        print(f"{pair["char"]}: {pair["num"]}")
    print("============= END ===============")

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    return

main()