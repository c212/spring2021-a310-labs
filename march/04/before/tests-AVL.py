from AVL import *

a = AVL(3)
a.insert(AVL(1))
a.insert(AVL(5))
a.insert(AVL(4))
a.display()
print("depth is: ", a.depth())

#  3_
# /  \
# 1  5
#   /
#   4
# depth is:  3
# 
