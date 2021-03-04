from BST import *

class AVL(BST):
  def depth(self):
    if self.left == None and self.right == None:
      return 1
    elif self.left == None:
      return 1 + self.right.depth()
    elif self.right == None:
      return 1 + self.left.depth()
    else:
      return 1 + max(self.left.depth(), self.right.depth())
  def balance(self):
    if self.left == None and self.right == None:
      return 0
    elif self.left == None:
      return 0 - self.right.depth()
    elif self.right == None:
      return self.left.depth()
    else:
      return self.left.depth() - self.right.depth()
