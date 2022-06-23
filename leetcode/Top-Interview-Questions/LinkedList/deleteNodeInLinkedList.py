class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteNode(node):
    # node.val = 5
    # node.next = 1
    node.val = node.next.val
    node.next = node.next.next
    

