def read(filename):
    with open(filename, 'r') as input:
        return input.read()
    
def contains(what, where):
    return what in read(where)

def file_rows_startingwith(start, filename):
    with open(filename, 'r') as input:
        return ''.join(line for line in input.readlines() if line.startswith(start))