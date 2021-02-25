filterArray = [0]*13

def h(string, size):
    sum = 0 
    for letter in string:
        sum = sum + ord(letter)
    return sum % size
print(h("Arsenal",len(filterArray)))
