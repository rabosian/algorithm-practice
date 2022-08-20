# In-order Traversal: left root right
# Pre-order Traversal: root left right
# Post-order Traversal: left right root

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal_recursion(root):
    result = []
    def dfs(root):
        # EDGE CASE!!!
        if not root:
            return
        if root.left:
            dfs(root.left)
        result.append(root.val)
        if root.right:
            dfs(root.right)
    dfs(root)
    return result


def inorderTraversal_iteration(root):
    result = []
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        
        if not stack:
            return result

        cur = stack.pop()
        result.append(cur.val)
        root = cur.right



            
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.right = n2
n2.left = n3

print(inorderTraversal_recursion(n1))
# print(inorderTraversal_iteration(n1))