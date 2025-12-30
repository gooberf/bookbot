def get_book_text(file_path:str):
    with open(file_path) as f:
        contents = f.read()
        return contents
