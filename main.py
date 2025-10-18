from stats import get_num_words
from stats import get_frequency_chars

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    
def sort_on(items):
    return items["num"]

def main():
    path = "books/frankenstein.txt"

    contents = get_book_text(path)
    num_words = get_num_words(contents)

    freq_dict = get_frequency_chars(contents)
    freq_dict = freq_dict.sort(reverse=True, key = sort_on)

    print("============ BOOKBOT ============")
    print("Analyzing book found at " + path+"...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print(freq_dict)

main()