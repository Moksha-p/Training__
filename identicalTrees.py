class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isIdentical(tree1, tree2):
    # If both trees are empty, they are identical
    if not tree1 and not tree2:
        return True
    
    # If one of the trees is empty and the other is not, they are not identical
    if not tree1 or not tree2:
        return False

    return (tree1.val == tree2.val and
            isIdentical(tree1.left, tree2.left) and
            isIdentical(tree1.right, tree2.right))