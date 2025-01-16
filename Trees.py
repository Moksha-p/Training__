# Binary Tree Solutions

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 1. Binary Tree Inorder Traversal
def inorder_traversal(root):
    def traverse(node):
        if not node:
            return []
        return traverse(node.left) + [node.val] + traverse(node.right)
    return traverse(root)

# Example for Inorder Traversal
tree = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(inorder_traversal(tree))  # Output: [1, 3, 2]

# 2. Maximum Depth of a Binary Tree
def max_depth(root):
    if not root:
        return 0
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    return max(left_depth, right_depth) + 1

# Example for Maximum Depth
tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(max_depth(tree))  # Output: 3

# 3. Check if Two Trees are Identical
def are_identical(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2 or t1.val != t2.val:
        return False
    return are_identical(t1.left, t2.left) and are_identical(t1.right, t2.right)

# Example for Identical Trees
tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
tree2 = TreeNode(1, TreeNode(2), TreeNode(3))
print(are_identical(tree1, tree2))  # Output: True

# 4. Level Order Traversal
def level_order_traversal(root):
    if not root:
        return []
    from collections import deque
    queue = deque([root])
    result = []

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result

# Example for Level Order Traversal
tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(level_order_traversal(tree))  # Output: [[1], [2, 3], [4, 5]]

# 5. Diameter of a Binary Tree
def diameter_of_binary_tree(root):
    diameter = 0

    def depth(node):
        nonlocal diameter
        if not node:
            return 0
        left_depth = depth(node.left)
        right_depth = depth(node.right)
        diameter = max(diameter, left_depth + right_depth)
        return max(left_depth, right_depth) + 1

    depth(root)
    return diameter

# Example for Diameter of Binary Tree
tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(diameter_of_binary_tree(tree))  # Output: 3
