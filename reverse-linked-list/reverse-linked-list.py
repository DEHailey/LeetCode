# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        
        current = head
        prev = None
        
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            
        return prev
        