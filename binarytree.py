class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    def traverse(node, result):
        if node:
            traverse(node.left, result)  # Traverse left subtree
            result.append(node.val)     # Visit root node
            traverse(node.right, result)  # Traverse right subtree
    
    result = []
    traverse(root, result)
    return result

