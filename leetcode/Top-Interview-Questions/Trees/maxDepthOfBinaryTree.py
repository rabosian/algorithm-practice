# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    if root is None:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1


print(max(None, 1))
root = TreeNode(3) 
root.left = TreeNode(9) 
root.right = TreeNode(20) 
root.right.left = TreeNode(15) 
root.right.right = TreeNode(7) 

print(maxDepth(root))