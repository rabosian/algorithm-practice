class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA, headB):
    if headA is None or headB is None:
        return
    a, b = headA, headB
    while a is not b:
        a = headB if not a else a.next
        b = headA if not b else b.next

    return a

