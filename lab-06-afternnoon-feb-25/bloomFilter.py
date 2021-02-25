filterArray = [0]*13

def h(string, size):
    sum = 0 
    for letter in string:
        sum = sum + ord(letter)
    return sum % size
print(h("Arsenal",len(filterArray)))

def h2(string,size):
    sum=0 
    count = 0
    for letter in string:
        count = count +1
        sum = sum + 2*count + ord(letter)
    return sum % size

print(h2("Arsenal",len(filterArray)))
