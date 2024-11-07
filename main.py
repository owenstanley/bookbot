def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    character_count = count_characters(text)
    generate_report(book_path, word_count, character_count)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_characters(text):
    characters = {}
    lower_t = text.lower()

    for char in lower_t:
        if char.isalpha():
            if char in characters:
                characters[char] = characters[char] + 1
            else:
                characters[char] = 1

    return characters

def convert_to_list_dict(dict):
    l = []
    for key in dict:
        d = {}
        d["character"] = key
        d["num"] = dict[key]
        l.append(d)

    return l

def sort_on(dict):
    return dict["num"]


def generate_report(book_path, word_count, character_count):
    char_list = convert_to_list_dict(character_count)
    char_list.sort(reverse=True, key=sort_on)
    print("--- Begin report of", book_path, "---" )
    print(word_count, "words found in the document")
    for dict in char_list:
        print("The character", dict["character"], "was found", dict["num"], "times.")
    print("--- End report ---")

main()