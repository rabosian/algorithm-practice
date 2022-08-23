# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    
    return values == values[::-1]
