# class Node:
#     def __init__(self, info):
#         self.info = info
#         self.left = None
#         self.right = None
#         self.level = None

#     def __str__(self):
#         return str(self.info)

# pre-order traversal (root left right)
def preOrder(root):
  print(root.info, end=" ")
  if root.left:
    preOrder(root.left)
  if root.right:
    preOrder(root.right)

# in-order traversal (left root right)
def preOrder(root):
  if root.left:
    preOrder(root.left)
  print(root.info, end=" ")
  if root.right:
    preOrder(root.right)

# post-order traversal (left right root)
def preOrder(root):
  if root.left:
    preOrder(root.left)
  if root.right:
    preOrder(root.right)
  print(root.info, end=" ")