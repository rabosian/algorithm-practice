from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# use BFS O(N)
# 1. save node in queue
# 2. if queue is empty, append all element in list
# 3. add children nodes to queue
def levelOrder(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        qLen = len(queue)
        level = []
        for i in range(qLen):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


 
root = TreeNode(3) 
root.left = TreeNode(9) 
root.right = TreeNode(20) 
root.right.left = TreeNode(15) 
root.right.right = TreeNode(7) 

print(levelOrder(root))