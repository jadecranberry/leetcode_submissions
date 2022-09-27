# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return 
        
        #find middle of list:
        slow = fast = head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
        #reverse linked list
        prev, curr = None, slow
        while curr:
            next_temp=curr.next
            curr.next=prev
            prev=curr
            curr=next_temp

        #merge two lists
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            
            second.next, second = first, second.next