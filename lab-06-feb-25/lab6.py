filter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def hash(string, size):
    sum = 0
    for letter in string:
        sum = sum + ord(letter)
    # print(sum)

    return sum % size

print(hash("morning", len(filter)))
