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
    if self.left == None: left = None
    else: left = self.left.adjust()
    if self.right == None: right = None
    else: right = self.right.adjust()
    return AVL(self.key + 1, left, right)
  #-------------(all three functions are purely functional)-------------

