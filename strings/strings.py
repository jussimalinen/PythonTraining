def length(text):
    return len(text)

def without(text, to_remove):
    return "".join(letter for letter in text if letter not in to_remove)

def count_distinct(text):
    return len(set(text))

def tokens(text):
    return [entry for entry in text.split('.') if entry]
