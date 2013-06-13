def add(*numbers):
    return sum(numbers)

def multiply(a,b):
    return  int(a)*int(b)

def divide(a,b):
    return a/b if b!=0 else 0

def add_two_largest(*numbers):
    return return sum(sorted(numbers)[-2:])
    
