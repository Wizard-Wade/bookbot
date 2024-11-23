path_to_file = "books/frankenstein.txt"

def main():
    text = get_book_text(path_to_file)
    num_words = get_num_words(text)
    letter_count = get_letters(text)
    print(letter_count)
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_letters(text):
    lower_text = text.lower()
    alphabet_dict = {}
    for char in lower_text:
        if char in alphabet_dict:
            alphabet_dict[char] +=1
        else:
            alphabet_dict[char] = 1
    return alphabet_dict
            
    
def get_book_text(path):
    with open(path) as f:
        return f.read()
        
main()