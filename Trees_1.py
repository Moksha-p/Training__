class TreeNode:
    def __init__(self,root):
        self.root = root
        self.left = None
        self.right = None

def inor_traversal(head):
    if head is None:
        return
    
    inor_traversal(head.left)

    print(head.root , end=' ')

    inor_traversal(head.right)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("In-Order Traversal: ", end="")
    inor_traversal(root)
    print()
    

