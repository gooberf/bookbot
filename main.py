from stats import word_count
from stats import char_count
from stats import sorting_thingy_majigy
import sys

def get_book_text(file_path:str):
    with open(file_path) as f:
        contents = f.read()
        return contents

def main(file_path:str):
    text = get_book_text(file_path)
    num_words = word_count(text)
    character_count = char_count(text)
    sorted_dict = sorting_thingy_majigy(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_dict:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


if len(sys.argv) >= 2:
    filepath = sys.argv[1]
    main(filepath)
else:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

