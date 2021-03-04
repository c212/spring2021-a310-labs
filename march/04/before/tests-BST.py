from BST import *

num = 6
a = BST(num)
print("Start from empty, insert ", num)
a.display()
num = 3
print("----Now insert ", num)
a.insert(num)
a.display()
print("---And insert 2:")
a.insert(2)
a.display()
numbers = [7, 9, 0, 8, 1, 4, 5]
print("---And insert (in order): ", numbers)
for num in numbers:
  a.insert(num)
a.display()

# Start from empty, insert  6
# 6
# ----Now insert  3
#  6
# / 
# 3 
# ---And insert 2:
#   6
#  / 
#  3 
# /  
# 2  
# ---And insert (in order):  [7, 9, 0, 8, 1, 4, 5]
#     __6   
#    /   \  
#    3   7_ 
#   / \    \
#  _2 4    9
# /    \  / 
# 0    5  8 
#  \        
#  1        
