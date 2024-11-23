path_to_file = "books/frankenstein.txt"

def main():
    text = get_book_text(path_to_file)
    num_words = get_num_words(text)
    print(num_words)
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
        
main()