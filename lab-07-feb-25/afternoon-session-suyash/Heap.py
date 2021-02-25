class Heap:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def size(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return 1 + self.right.size()
        elif self.right is None:
            return 1 + self.left.size()
        else:
            return 1 + self.left.size() + self.right.size()

    def depth(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return 1 + self.right.depth()
        elif self.right is None:
            return 1 + self.left.depth()
        else:
            return 1 + max(self.left.depth(), self.right.depth())

    def insert(self, key):
        if self.left is None and self.right is None:
            self.left = Heap(key)
        elif self.right is None:
            self.right = Heap(key)
        else:
            leftDepth = self.left.depth()
            leftSize = self.left.size()
            rightDepth = self.right.depth()
            rightSize = self.right.size()

            if leftSize < 2 ** leftDepth - 1:
                self.left.insert(key)
            elif leftSize == (2 ** leftDepth -1 ) and rightSize < leftSize:
                self.right.insert(key)
            else:
                self.left.insert(key)


    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

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


h = Heap(1)
print(" Inserting the value ", 1)
h.display()

for i in range(2,10):
    print(" Inserting the value ", i)
    h.insert(i)
    h.display()