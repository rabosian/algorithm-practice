class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    num1 = l1.val
    num2 = l2.val
    i = 10
    while l1.next or l2.next:
        if l1.next:
            num1 += l1.next.val * i
            l1 = l1.next

        if l2.next:
            num2 += l2.next.val * i
            l2 = l2.next
        i *= 10

    temp = list(str(num1+num2))
    result = ListNode(temp[-1])
    head = result
    for i in range(len(temp)-2, -1, -1):
        print(result.val)
        result.next = ListNode(temp[i])
        result = result.next
    return head

# l1 2 4 3
# l2 5 6 4
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = addTwoNumbers(l1, l2)

