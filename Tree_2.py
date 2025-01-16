
class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def height(root):
    if root is None:
        return -1


    left_hei = height(root.left)
    reight_hei = height(root.right)

    return max(left_hei, reight_hei) + 1



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(height(root))