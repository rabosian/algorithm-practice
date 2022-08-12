# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS recursion: O(N)
def maxDepth(root):
    if root is None:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


# DFS iteration:
def maxDepth_iterative(root):
    stack = [[root, 1]]
    depth = 0
    while stack:
        node, level = stack.pop()
        if node:
            depth = max(depth, level)
            stack.append([node.left, level+1])
            stack.append([node.right, level+1])
    return depth


# BFS recursion: O(N)
def maxDepth_bfs(root):
    if not root:
        return 0
    queue, depth = deque([root]), 0
    while queue:
        for i in range(len(queue)):
            cur = queue.popleft()
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        depth += 1
    return depth


root = TreeNode(3) 
root.left = TreeNode(9) 
root.right = TreeNode(20) 
root.right.left = TreeNode(15) 
root.right.right = TreeNode(7) 

print(maxDepth_iterative(root))