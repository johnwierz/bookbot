

def get_word_count(text):
    words = text.split()
    word_count = len(words)
    print(f"Found {word_count} total words")

# new function that takes the text from the book as a string
# function then returns the number of times each character (including symbols and spaces) appears in the string
# convert any character to lowercase using .lower(), no duplicates
# use a dictionary of string -> integer
# ergo {'p': 6121, 'r': 20818, 'o': 25225, ...}


def character_count(text):
    lower_case = text.lower()
    words = lower_case.split()
    all_characters = [char for word in words for char in word]
    unique_characters = []
    for char in all_characters:
        if char not in unique_characters:
            unique_characters.append(char)
    character_counts = {}
    for char in unique_characters:
        character_counts[char] = all_characters.count(char)
    #unique_characters = list(set(all_characters))
    return character_counts
    
#def make_list(character_counts):
#    character_counts_list = ["char", "num"]    

def sort_on(character_counts_list):
    return character_counts_list["num"]



def sort_dictionary(character_counts):
    character_counts_list = []
    for char, num in character_counts.items():
        if char.isalpha():
            character_counts_list.append({ "char": char, "num": num})
    character_counts_list.sort(key=sort_on, reverse=True)
    for item in character_counts_list:
        print(f"{item['char']}: {item['num']}")
    

#    sorted_values = sorted(character_counts.values())
#    print(sorted_values)
