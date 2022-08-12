def isPalindrome(head):
    if not head or not head.next:
        return True
    # array method    
    # nums = []
    # while head:
    #     nums.append(head.val)
    #     head = head.next
    # if nums == nums[::-1]:
    #     return True
        
    # two pointer method -> O(1) space
    fast, slow = head, head
    # 1. find mid point
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next  
    
    # 2. reverse second half
    prev = None
    while slow:
        next = slow.next
        slow.next = prev
        prev = slow
        slow = next
    
    # 3. check palindrome
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True

