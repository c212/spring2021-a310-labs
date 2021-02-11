class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVL_Tree(object):

    def insert(self,root, key):

        if not root:
            return TreeNode(key)
        elif key<root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

    #     case 1 - left left
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)
        # case 2 - right right
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)
        # Case 3 Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # case 4 Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root
    def getHeight(self, root):
        if not root:
            return 0

        return root.height

    def getBalance(self, root):
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)



    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))

        return y

    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def delete(self, root, key):
        if not root:
            return root

        elif key < root.val:
            root.left = self.delete(root.left, key)

        elif key > root.val:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.getMinValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        # Case 1  left left

        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)

    #     case 2 right right
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)
    #     Case 3 Left Right
        if balance > 1 and self.getBalance(root.left) < 0 :
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        #     Case 4 Right Left
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root
    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

# tree = AVL_Tree()
# root = TreeNode(7)
# tree.insert(root, 3)
# tree.insert(root, 17)
# tree.insert(root,5)
# tree.insert(root, 13)
# print(root.right.val)
# new_root = tree.insert(root,15)
#
# print(new_root.right.val)

tree = AVL_Tree()

root = TreeNode(17)
tree.insert(root, 7)
tree.insert(root, 21)
tree.insert(root, 13)
print(root.val)
new_root = tree.delete(root, 17)
print(new_root.val)