filter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 0 - 12, 13 total

def hash(string, size):
    sum = 0
    for letter in string:
        sum = sum + ord(letter)
    # print(sum)

    return sum % size

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
        sum = sum + ord(letter)
    return ((sum + 2) * 5) % size

def conversion (string, size):
    return (hash(string, size)),(hash2(string, size)),(hash3(string, size))

def insert(filter, word):
    tuple = conversion(word, len(filter))
    for num in tuple:
        filter[num] = 1
    print(tuple)

def find(filter, word):
    tuple = conversion(word, len(filter))
    for num in tuple:
        if filter[num] == 0:
            return False
    return True

print("First hash example results")
print(hash("morning", len(filter))) #in the sample, 8 and 10
print(hash("sunshine", len(filter))) #in the sample, 5 and 6
print(hash("lecture", len(filter)))
#If a word is 5 and 10, the Bloom filter says it might be in the set
#In the sample, "tight" fnv = 10, and murmur = 8, so it is a maybe

print("Second hash example results")
print(hash2("morning", len(filter))) 
print(hash2("sunshine", len(filter)))
print(hash2("lecture", len(filter)))

print("Third hash example results")
print(hash3("morning", len(filter))) 
print(hash3("sunshine", len(filter)))
print(hash3("lecture", len(filter)))

print(conversion("morning", len(filter)))
insert(filter, "hello")
print(filter)
print(find(filter, "hello"))
print(find(filter, "dog"))
