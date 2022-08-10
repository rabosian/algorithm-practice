def removeNthFromEnd(head, n):
    slow, fast = head, head

    for _ in range(n):
        fast = fast.next
    
    if not fast:
        return None
    if not fast.next:
        slow.next = slow.next.next
        return head
    while fast.next:
        slow = slow.next
        fast = fast.next
    # slow  == Nth node from end

    slow.next = slow.next.next
    return head

    