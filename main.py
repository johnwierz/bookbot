import sys
from stats import get_word_count
from stats import character_count
from stats import sort_dictionary

print("============ BOOKBOT ============")


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return(file_contents)

def main():
    if len(sys.argv) == 2:
        text = get_book_text(sys.argv[1]) #change the argument to "books/frankenstein.txt" to return to normal
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        get_word_count(text)
        character_counts = character_count(text)
        print("--------- Character Count -------")
        sort_dictionary(character_counts)
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 



main()