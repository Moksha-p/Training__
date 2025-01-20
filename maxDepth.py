class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    # Base case: if the tree is empty, depth is 0
    if not root:
        return 0
    
    # Recursively find the depth of left and right subtrees
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    
    # Maximum depth is 1 (current node) + max depth of left or right subtree
    return 1 + max(left_depth, right_depth)