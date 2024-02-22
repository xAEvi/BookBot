FILE_PATH = 'books/frankenstein.txt'

def main():
    book = get_book()
    words = get_words(book)
    counted_words = count_words(words)

    counted_list = dict_to_list_dict(counted_words)

    print_report(counted_list)

def get_book():
    with open(FILE_PATH) as f:
        file_content = f.read()

    return file_content

def get_words(book):
    return book.split()

def count_words(words):
    dictionary = {}

    for word in words:
        for letter in word.lower():
            if letter not in dictionary:
                dictionary[letter] = 1
            else: 
                dictionary[letter] += 1

    return dictionary

def dict_to_list_dict(data):
    return [{'letter': key, 'frequency': value} for key, value in data.items()]

def print_report(words):
    words.sort(reverse=True, key=sort_on)
    
    print(f'--- Being report of {FILE_PATH }')
    for word in words:
        letter = word['letter']
        count = word['frequency']
        if letter.isalpha():
            print(f'The {letter} character was found {count} times')

def sort_on(dict):
    return dict['frequency']
main()