filter = [0]*13
def hash(string, size):
    sum = 0
    for letter in string:
        sum = sum + ord(letter)
    return sum%size
def hash2(string, size):
    sum = 0
    count = 0
    for letter in string:
        count = count + 1
        sum = sum + 3*count + ord(letter)
    return sum % size
def hash3(string, size):
    sum = 0
    for letter in string:
        sum = sum +ord(letter)
    return  ((sum+2) *5) %size

def conversion(string, size):
    return(hash(string, size),hash2(string, size),hash3(string, size))


print(hash("morning", len(filter)))
print(hash("sunshine", len(filter)))
print(hash("lecture",len(filter)))
print(hash2("morning", len(filter)))
print(hash2("sunshine", len(filter)))
print(hash2("lecture",len(filter)))
print(hash3("morning", len(filter)))
print(hash3("sunshine", len(filter)))
print(hash3("lecture",len(filter)))
print(conversion("morning",len(filter)))

