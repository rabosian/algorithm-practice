class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

# pre-order traversal
def pre_order(node):
    print(node.data, end=' ')
    if node.left:
        pre_order(tree[node.left])
    if node.right:
        pre_order(tree[node.right])

# in-order traversal
def in_order(node):
    if node.left:
        in_order(tree[node.left])
    print(node.data, end=' ')
    if node.right:
        in_order(tree[node.right])

# post-order traversal
def post_order(node):
    if node.left:
        post_order(tree[node.left])
    if node.right:
        post_order(tree[node.right])
    print(node.data, end=' ')


n = int(input())
tree = {}

for i in range(n):
    data, left, right = input().split()
    if left == "None":
        left = None
    if right == "None":
        right = None
    tree[data] = Node(data, left, right)


print("pre-order traverse:")
pre_order(tree['A'])
print()
print("in-order traverse:")
in_order(tree['A'])
print()
print("post-order traverse:")
post_order(tree['A'])
