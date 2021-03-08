from AVL import *

import re
num = input("Enter the first number: ")
a = AVL(int(num)) # please be careful here 
a.display()
while True:
  num = input("Enter command: ")
  if num == 'bye':
    break
  else:
    m = re.search('(\w+)\s+(\d+)', num)
    command = m.group(1)
    number = int(m.group(2))
    if command == 'insert':
      a.insert(AVL(number)) # and here (of course)
      a.display()
    else:
      print("I don't understand ", command)

#---- this is how it works: 
#  
# Enter the first number: 5
# 5
# Enter command: insert 2
#  5
# / 
# 2 
# Enter command: insert 4
#  _5
# /  
# 2  
#  \ 
#  4 
# Enter command: insert 3
#  __5
# /   
# 2_  
#   \ 
#   4 
#  /  
#  3  
# Enter command: insert 1
#   __5
#  /   
#  2_  
# /  \ 
# 1  4 
#   /  
#   3  
# Enter command: insert 7
#   __5 
#  /   \
#  2_  7
# /  \  
# 1  4  
#   /   
#   3   
# Enter command: insert 9
#   __5  
#  /   \ 
#  2_  7 
# /  \  \
# 1  4  9
#   /    
#   3    
# Enter command: insert 6
#   __5_  
#  /    \ 
#  2_   7 
# /  \ / \
# 1  4 6 9
#   /     
#   3     
# Enter command: insert 8
#   __5_   
#  /    \  
#  2_   7_ 
# /  \ /  \
# 1  4 6  9
#   /    / 
#   3    8 
# Enter command: bye
# >>> 
