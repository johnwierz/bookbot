def get_num_words(text):
    words = text.split()
    return len(words)

def analyze_characters(text):
    characters = text.split()
    lower_characters = characters.lower()
    return lower_characters