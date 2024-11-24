path_to_file = "books/frankenstein.txt"

def main():
    text = get_book_text(path_to_file)
    num_words = get_num_words(text)
    letter_count = get_letters(text)
    sort = sort_letters(letter_count)
    
    
    print("--- Begin report of books/frankenstein.txt ---")
    print (num_words)
    for key, value in sort.items():
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")
    
def sort_letters(dict_letters):
    sort = dict(sorted(dict_letters.items(),key= lambda item : item[1], reverse=True))
    return sort
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_letters(text):
    lower_text = text.lower()
    alphabet_dict = {}
    for char in lower_text:
        if not char.isalpha():
            continue
        if char in alphabet_dict:
            alphabet_dict[char] +=1
        else:
            alphabet_dict[char] = 1
    return alphabet_dict
            
    
def get_book_text(path):
    with open(path) as f:
        return f.read()
        
main()