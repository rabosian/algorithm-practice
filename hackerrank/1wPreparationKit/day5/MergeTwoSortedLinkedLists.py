# headA: 1 3 7 null
# headB: 1 2 null
# newList: 1 1 2 3 7 null
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next

def mergeLists(head1, head2):
    if None in (head1, head2):
        return head1 or head2

    dummy = SinglyLinkedList(0)
    tail = dummy

    while head1 and head2:
        if head1.data < head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next
    tail.next = head1 if head1 else head2

    return dummy.next


def mergeLists_recursive(head1, head2):
    if None in (head1, head2):
        return head1 or head2
    
    if head1.data <= head2.data:
        head1.next = mergeLists_recursive(head1.next, head2)
        return head1
    else:
        head2.next = mergeLists_recursive(head1, head2.next)
        return head2