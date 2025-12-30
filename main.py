def get_book_text(file_path:str):
    with open(file_path) as f:
        contents = f.read()
        return contents

def word_count(text:str):
    num_words = 0
    words = text.split()
    for word in words: num_words += 1
    return num_words

def main(file_path:str):
    num_words = word_count(get_book_text(file_path))
    print(f'Found {num_words} total words')

main('books/frankenstein.txt')