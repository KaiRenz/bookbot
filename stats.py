def get_num_words(file_contents):
    return(len(file_contents.split()))

def get_num_characters(file_contents):
    characters =  {}
    text_lowercase = file_contents.lower()
    for c in text_lowercase:
        if c not in characters:
            characters[c] = 1
        else:
            characters[c] = characters[c] + 1
    return(characters)

def convert_dictionary_to_list(file_contents):
    characters =  {}
    text_lowercase = file_contents.lower()
    for c in text_lowercase:
        if c not in characters:
            characters[c] = 1
        else:
            characters[c] = characters[c] + 1
    
    character_list = []
    for character in characters:
        character_list.append({"char": character, "num": characters[character]})
    
    return character_list

def sort_on(items):
    return items["num"]