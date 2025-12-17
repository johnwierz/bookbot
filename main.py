from stats import get_word_count
from stats import character_count
from stats import sort_dictionary

print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return(file_contents)

def main():
    text = get_book_text("books/frankenstein.txt")
    print("----------- Word Count ----------")
    get_word_count(text)
    character_counts = character_count(text)
    print("--------- Character Count -------")
    sort_dictionary(character_counts)
    print("============= END ===============")

main()