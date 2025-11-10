from stats import get_word_count
from stats import character_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return(file_contents)

def main():
    text = get_book_text("books/frankenstein.txt")
    get_word_count(text)
    character_count(text)

main()