import re
book = {}

def add(name, number):
    if not _valid_number(number) or not _valid_name(name):
        return False
    book[name] = number
    return True

def _valid_number(number):
    return re.match("\+?[\d ]+$", number)

def _valid_name(name):
    return re.match("[\w ]+$", name)

def get(name):
    return book[name] if name in book else "Unknown"

def clear():
    book.clear()
    
def _to_string():
    result = ""
    for name in sorted(book.keys()):
        result += "%s=%s\n" % (name, book[name])
    return result

def _read(content):
    for line in content.splitlines():
        name, number = line.split("=")
        add(name, number.strip())
        
def save(filename):
    with open(filename, "w") as out:
        out.write(_to_string())
        
def load(filename):
    with open(filename, "r") as input:
        _read(input.read())

