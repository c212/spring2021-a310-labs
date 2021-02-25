filter = [0]*13
def hash(string, size):
    sum = 0
    for letter in string:
        sum = sum + ord(letter)
    return sum%size

print(hash("morning", len(filter)))

