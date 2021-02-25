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



print(hash("morning", len(filter)))
print(hash("sunshine", len(filter)))
print(hash2("morning", len(filter)))
print(hash2("sunshine", len(filter)))

