# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# idea 1. using in-order traverse
def isValidBST_in_order(root):
    treeList = []
    def treeToList(root, treeList):
        if root:
            treeToList(root.left, treeList)
            treeList.append(root.val)
            treeToList(root.right, treeList)

    treeToList(root, treeList)
    return (len(treeList) == len(set(treeList))) and (treeList == sorted(treeList))


# idea 2. set boundaries of each node: O(N)
def isValidBST(root):
    def validate(root, left, right):
        if not root:
            return True
        if not (root.val < right and root.val > left):
            return False
        return (validate(root.left, left, root.val) and validate(root.right, root.val, right))
    
    return validate(root, float('-inf'), float('inf'))


root = TreeNode(5) 
root.left = TreeNode(2) 
root.right = TreeNode(9) 
root.left.left = TreeNode(1) 
root.left.right = TreeNode(4) 
root.right.left = TreeNode(6) 
root.right.right = TreeNode(11) 

print(isValidBST(root))