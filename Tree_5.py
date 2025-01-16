
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return 0

    return 1 + max(height(root.left), height(root.right))


def diameter(root):
    if root is None:
        return 0


    lheight = height(root.left)
    rheight = height(root.right)


    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)


    return max(lheight + rheight, ldiameter, rdiameter)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


print(diameter(root))