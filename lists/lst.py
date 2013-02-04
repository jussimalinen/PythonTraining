def sort(*lst):
    return sorted(lst)

def maximum(*lst):
    return max(int(value) for value in lst)

def positives(*lst):
    return [value for value in lst if value > -1]