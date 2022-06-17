import math
# ListNode !!!


def middleNode(head):
    # mid = math.ceil((head[0] + head[-1]) / 2)
    # return head[mid-1:]
    slow = fast = head
    while fast and fast.next:
        slow = slow.next # move 1 step
        fast = fast.next.next # move 2 steps
        # fast has 2x moving speed than slow.
        # so the time fast reach to the end, slow would be half way to the end
    return slow

# Time complexity   O(N), N is the number of nodes in the given list
# Space complexity  O(1) used by slow and fast


