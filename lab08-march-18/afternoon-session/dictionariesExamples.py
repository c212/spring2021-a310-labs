import pprint

# spam = {'color': ['red',' blue' ], 'age': {'name': 'aman', 'val': 42}}
#
# print(spam)
#
# pprint.pprint(spam)
#
# print(spam['color'])
#
# print(spam.keys())
#
# for key, value in spam.items():
#     print(key, value)
#
# if 'name' in spam:
#     print("True")
# else:
#     print("False")

# Fantasy Game inventory
'''
Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62
'''

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def displayInventory(inv):
    sum = 0
    print("Inventory:")
    for key, value in inv.items():
        sum += value
        print(value, key)
    print("Total number of items:", sum)


def addToInventory(inv, listInv):
    for item in listInv:
        if item in inv:
            inv[item] += 1
        else:
            inv[item] = 1
    return inv


displayInventory(stuff)
stuff = addToInventory(stuff, dragonLoot)

displayInventory(stuff)
