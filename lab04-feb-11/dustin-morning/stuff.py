class BstNode:
  def __init__(self, key):
    self.key = key
    self.right = None
    self.left = None

  def setLeft(self, left):
    self.left = left
    
  def setRight(self, key):
    self.right = BstNode(key)

  def display(self):
    lines, *_ = self._display_aux()
    for line in lines:
      print(line)

  # find returns a Boolean value indicating ... 
  def find(self, value):
    print ("Now looking at: ", self.key)
    if value == self.key:
      return True
    else:
      one = False # if no left child I am done already
      two = False
      if self.left != None: # have left child
        one = self.left.find(value)
      if not one and self.right != None: # have right child
        two = self.right.find(value)
      return one or two

  def _display_aux(self):
    """Returns list of strings, width, height, and horizontal coordinate of the root."""
    # No child.
    if self.right is None and self.left is None:
      line = '%s' % self.key
      width = len(line)
      height = 1
      middle = width // 2
      return [line], width, height, middle
    # Only left child.
    if self.right is None:
      lines, n, p, x = self.left._display_aux()
      s = '%s' % self.key
      u = len(s)
      first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
      second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
      shifted_lines = [line + u * ' ' for line in lines]
      return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
    # Only right child.
    if self.left is None:
      lines, n, p, x = self.right._display_aux()
      s = '%s' % self.key
      u = len(s)
      first_line = s + x * '_' + (n - x) * ' '
      second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
      shifted_lines = [u * ' ' + line for line in lines]
      return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
    # Two children.
    left, n, p, x = self.left._display_aux()
    right, m, q, y = self.right._display_aux()
    s = '%s' % self.key
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
      left += [n * ' '] * (q - p)
    elif q < p:
      right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2

root = BstNode(3)
a = root
a.setLeft(BstNode(5))
b = a.left
b.setRight(1)
b.setLeft(BstNode(7))

a = BstNode(10)
root.setRight(12)
root.right.setRight(16)
root.right.right.setLeft(a) # 3 ( 5( 7 ( : ) : 1 ( : )) : 12 ( : 16 ( 10 ( : ) : ) ) )

root.display()

# for i in range(17):
#   print(i, ": ", root.find(i))

# depth first 
