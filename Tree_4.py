
class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def levelOrderRec(root, level, res):
    if not root:
        return

   
    if len(res) <= level:
        res.append([])


    res[level].append(root.data)


    levelOrderRec(root.left, level + 1, res)
    levelOrderRec(root.right, level + 1, res)

def levelOrder(root):
    res = []
    levelOrderRec(root, 0, res)
    return res
      


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)



res = levelOrder(root)


for level in res:
    for data in level:
        print(data, end=" ")