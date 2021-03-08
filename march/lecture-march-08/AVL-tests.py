from AVL import *

a = AVL(3)
a.insert(AVL(1))
a.insert(AVL(5))
a.insert(AVL(4))
a.display()
print("root depth is: ", a.depth())
print("root balance is: ", a.balance())

a = a.adjust() # this is the new addition 

a.display() # <-- a bit contrived adjust does not balance anything just adds 1 to every node
# notice also adjust is purely functional, returns new tree altogether try: a.adjust().display()

print("root depth is: ", a.depth())
print("root balance is: ", a.balance())

#   3_
#  /  \
#  1  5
#    /
#    4
#  root depth is:  3
#  root balance is:  -1
#   4_
#  /  \
#  2  6
#    /
#    5
#  root depth is:  3
#  root balance is:  -1

