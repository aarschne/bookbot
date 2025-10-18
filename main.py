from stats import get_num_words
from stats import get_frequency_chars
from stats import sort_dict
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    
def print_dict_list(dict_list):
    for i in range(0,len(dict_list)):
        print(f"{dict_list[i]["char"]}: {dict_list[i]["num"]}")
    


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]

    contents = get_book_text(path)
    num_words = get_num_words(contents)

    freq_dict = get_frequency_chars(contents)
    freq_dict = sort_dict(freq_dict)

    print("============ BOOKBOT ============")
    print("Analyzing book found at " + path+"...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print_dict_list(freq_dict)

main()