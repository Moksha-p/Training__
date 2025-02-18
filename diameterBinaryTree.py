class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root):
    max_diameter = [0]
    
    def depth(node):
        if not node:
            return 0
        
        # Recursively find the depth of the left and right subtrees
        left_depth = depth(node.left)
        right_depth = depth(node.right)

        max_diameter[0] = max(max_diameter[0], left_depth + right_depth)

        return 1 + max(left_depth, right_depth)
    
    depth(root)
    return max_diameter[0]