def get_book_text(file_path:str):
    with open(file_path) as f:
        contents = f.read()
        return contents

def word_count(text:str):
    

def main(file_path:str):
    print(get_book_text(file_path))

main('books/frankenstein.txt')