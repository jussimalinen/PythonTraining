def length(text):
    return len(text)

def without(text, to_remove):
    for letter in to_remove:
        text = text.replace(letter, '')
    return text

def count_distinct(text):
    return len(set(text))

def tokens(text):
    return [entry for entry in text.split('.') if entry!='']