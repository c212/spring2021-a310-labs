filterArray = [0]*13

def h(string, size):
    sum = 0
    for letter in string:
        sum = sum + ord(letter)
    return sum % size
print(h("Arsenal",len(filterArray)))

def h2(string, size):
    sum = 0
    count = 0
    for letter in string:
        count = count + 1
        sum = sum + 2*count + ord(letter)
    return sum % size

print(h2("Arsenal",len(filterArray)))

def h3(string, size):
    sum = 0
    count = 0
    for letter in string:
        count += 3
        sum = sum + 7* count + ord(letter)
    return sum % size

print(h3("Arsenal",len(filterArray)))

def insertName(name):
    val1 = h(name, len(filterArray))
    val2 = h2(name, len(filterArray))
    val3 = h3(name, len(filterArray))
    filterArray[val1] = 1
    filterArray[val2] = 1
    filterArray[val3] = 1

print(filterArray)
insertName("David")
print(filterArray)

def find(name, filterArray):
    hashValues = conversion(name, len(filterArray))
    for value in hashValues:
        if filterArray[value] == 0:
            return False
    return True

def conversion(name, size):
    return (h(name, size), h2(name, size), h3(name, size))

# print(conversion("josh", len(filterArray)))

insertName("Brandon")
insertName("Aman")

print(find("Brandon", filterArray))
print(find("Aman", filterArray))
print(find("Suyash", filterArray))




