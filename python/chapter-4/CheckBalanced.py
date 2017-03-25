class TreeNode(object):
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.data)

def CheckBalanced(root):
    height, balanced = CalHeight(root)
    return balanced

def CalHeight(root):
    if root is None:
        return -1, True
    hLeft, leftBalanced = CalHeight(root.left)
    hRight, rightBalanced = CalHeight(root.right)
    h = max(hLeft, hRight) + 1
    b = leftBalanced and rightBalanced
    if abs(hLeft - hRight) > 1:
        b = False
    return h, b

if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2, n1)
    n4 = TreeNode(4)
    n3 = TreeNode(3, n2, n4)
    n6 = TreeNode(6)
    n8 = TreeNode(8)
    n7 = TreeNode(7, n6, n8)
    n5 = TreeNode(5, n3, n7)
    print CheckBalanced(n5)

