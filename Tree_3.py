
class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def isIdentical(r1, r2):

    if r1 is None and r2 is None:
        return True

    if r1 is None or r2 is None:
        return False


    return (r1.data == r2.data and
            isIdentical(r1.left, r2.left) and
            isIdentical(r1.right, r2.right))




r1 = TreeNode(1)
r1.left = TreeNode(2)
r1.right = TreeNode(3)
r1.left.left = TreeNode(4)


r2 = TreeNode(1)
r2.left = TreeNode(2)
r2.right = TreeNode(3)
r2.left.left = TreeNode(4)

if isIdentical(r1, r2):
    print("Yes")
else:
    print("No")