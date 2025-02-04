from trees1 import TreeNode


def diameterOfBinaryTree(root):
    def helper(node):
        nonlocal diameter
        if not node:
            return 0
        left_depth = helper(node.left)
        right_depth = helper(node.right)
        diameter = max(diameter, left_depth + right_depth)
        return max(left_depth, right_depth) + 1
    
    diameter = 0
    helper(root)
    return diameter

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(diameterOfBinaryTree(root))
