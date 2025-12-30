def word_count(text:str):
    num_words = 0
    words = text.split()
    for word in words: num_words += 1
    return num_words

def char_count(text:str):
    char_dict = {}
    for letter in text:
        letter = letter.lower()
        if letter not in char_dict:
            char_dict[letter] = 1
        else:
            char_dict[letter] += 1
    return char_dict

def sorting_thingy_majigy(character_dict):
    dict_holder = []
    for char, count in character_dict.items():
        placeholder = {'char': char, 'num': count}
        dict_holder.append(placeholder)
    dict_holder.sort(reverse=True, key=sort_on)
    return dict_holder

def sort_on(item):
    return item['num']