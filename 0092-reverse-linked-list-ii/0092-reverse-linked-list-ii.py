# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head, m, n):
        if not head or m == n:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev_m = dummy
        
        for _ in range(m - 1):
            prev_m = prev_m.next
            
        curr = prev_m.next
        prev = None
        
        for _ in range(n - m + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        prev_m.next.next = curr
        prev_m.next = prev
    
        return dummy.next