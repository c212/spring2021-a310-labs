from BST import *

class AVL(BST):
  def depth(self): #--------------------------------------(depth)-----
    if self.left == None and self.right == None: return 1
    elif self.left == None: return 1 + self.right.depth()
    elif self.right == None: return 1 + self.left.depth()
    else: return 1 + max(self.left.depth(), self.right.depth())
  def balance(self): #------------------------------------(balance)---
    if self.left == None and self.right == None: return 0
    elif self.left == None: return 0 - self.right.depth()
    elif self.right == None: return self.left.depth()
    else: return self.left.depth() - self.right.depth()
  def adjust(self): #-------------------------------------(adjust)-----
    if self.left == None: (dl, left) = (0, None)
    else:
      left = self.left.adjust()
      dl = left.depth()
    if self.right == None: (dr, right) = (0, None)
    else:
      right = self.right.adjust()
      dr = right.depth()
    if dl - dr == -2: # tree would be right heavy 
      if right.balance() > 0: # LL (right subtree left heavy)
        return AVL(right.left.key, AVL(self.key, left, right.left.left), AVL(right.key, right.left.right, right.right))
      else: # L
        return AVL(right.key, AVL(self.key, left, right.left), AVL(right.right.key, right.right.left, right.right.right))
    elif dl - dr == 2: # tree would be left heavy
      if left.balance() < 0: # RR (left subtree right heavy)
        return AVL(left.right.key, AVL(left.key, left.left, left.right.left), AVL(self.key, left.right.right, right))
      else: # R
        return AVL(left.key, AVL(left.left.key, left.left.left, left.left.right), AVL(self.key, left.right, right))
    return AVL(self.key, left, right)
  
# =========== RESTART: C:\Users\dgerman\Desktop\march-08-lecture\AVL.py ===========
# >>> a = AVL(1)
# >>> a.display()
# 1
# >>> a.insert(AVL(2))
# >>> a.display()
# 1 
#  \
#  2
# >>> a.insert(AVL(3))
# >>> a.display()
# 1  
#  \ 
#  2 
#   \
#   3
# >>> a.adjust().display()
#  2 
# / \
# 1 3
# >>> a.display()
# 1  
#  \ 
#  2 
#   \
#   3
# >>> a = a.adjust()
# >>> a.display()
#  2 
# / \
# 1 3
# >>> a.insert(AVL(4))
# >>> a.display()
#  2  
# / \ 
# 1 3 
#    \
#    4
# >>> a.adjust().display()
#  2  
# / \ 
# 1 3 
#    \
#    4
# >>> a.insert(AVL(5))
# >>> a.display()
#  2   
# / \  
# 1 3  
#    \ 
#    4 
#     \
#     5
# >>> a.adjust().display()
#  2_  
# /  \ 
# 1  4 
#   / \
#   3 5
# >>> a.display()
#  2   
# / \  
# 1 3  
#    \ 
#    4 
#     \
#     5
# >>> a = a.adjust()
# >>> a.display()
#  2_  
# /  \ 
# 1  4 
#   / \
#   3 5
# >>> a.insert(AVL(6))
# >>> a.display()
#  2_   
# /  \  
# 1  4  
#   / \ 
#   3 5 
#      \
#      6
# >>> a = a.adjust() # basic step after insertion 
# >>> a.display()
#   _4  
#  /  \ 
#  2  5 
# / \  \
# 1 3  6
# >>> 

