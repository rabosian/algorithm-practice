class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    if None in (list1, list2):
        return list1 or list2
    result = ListNode(0)
    while list1 and list2:
        if list1.val < list2.val:
            result.val = list1.val
            result = result.next
            list1 = list1.next
        else:
            result.val = list2.val
            result = result.next
            list2 = list2.next


        # if None in (list1, list2):
        #     return list1 or list2
        # result = ListNode(0)
        # while list1 and list2:
        #     if list1.val < list2.val:
        #         result.val = list1.val
        #         list1 = list1.next
        #     else:
        #         result.val = list2.val
        #         list2 = list2.next
        # return result.val