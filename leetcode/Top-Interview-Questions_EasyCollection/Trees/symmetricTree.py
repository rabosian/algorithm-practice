# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# using in-order traverse (X) => cannot deal with repeated element
def isSymmetric_in_order(root):
    treeList = []
    def treeToList(root, treeList):
        if root:
            treeToList(root.left, treeList)
            treeList.append(root.val)
            treeToList(root.right, treeList)
    treeToList(root, treeList)
    return treeList[::-1] == treeList


def isSymmetric(root):
    if not root:
        return True
    stack = [(root.left, root.right)]
    while stack:
        left, right = stack.pop()
        if not left and not right:
            continue
        if not left or not right:
            return False
        if left.val == right.val:
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
        else:
            return False
    return True
    

root = TreeNode(1) 
root.left = TreeNode(2) 
root.right = TreeNode(2) 
root.left.left = TreeNode(3) 
root.left.right = TreeNode(4) 
root.right.left = TreeNode(4) 
root.right.right = TreeNode(3) 

print(isSymmetric(root))