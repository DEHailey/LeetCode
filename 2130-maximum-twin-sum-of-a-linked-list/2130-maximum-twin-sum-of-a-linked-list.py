# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head):
        if not head or not head.next:
            return 0
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        max_sum = 0
        left = head
        right = prev
        
        while left and right:
            max_sum = max(max_sum, left.val + right.val)
            left = left.next
            right = right.next
        
        return max_sum
            
        
        