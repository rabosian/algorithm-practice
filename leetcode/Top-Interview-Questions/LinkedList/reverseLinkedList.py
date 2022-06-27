# (i) three pointer method (iterative)
def reverseList_iterative(head):
    if head == None or head.next == None:
        return head
    prev = None # the last element's next == Null
    cur, next = head, head
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    head = prev
    return head


# (ii)recursive
def reverseList_recursive(head):
    if head == None or head.next == None:
        return head
    
    rest = reverseList_recursive(head.next)
    head.next.next = head
    head.next = None
    return rest
