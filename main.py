from stats import get_num_words, get_num_characters, convert_dictionary_to_list, sort_on
import sys

def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    num_words = get_num_words(get_book_text(filepath))
    print(f"Found {num_words} total words")

    num_characters = get_num_characters(get_book_text(filepath))
    print(num_characters)

    items = convert_dictionary_to_list(get_book_text(filepath))
    items.sort(reverse=True, key=sort_on)
    
    for item in items:
        print(f'{item["char"]}: {item["num"]}')

if __name__ == "__main__":
    main()