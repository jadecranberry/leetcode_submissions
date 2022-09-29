


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right:
            return head
        
        prev=None
        current=head
        i=1
        while current is not None and i<left:
            prev=current
            current=current.next
            i+=1
        
        left_node_1=prev
        left_node=current
        
        i=0
        while current is not None and i<right-left+1:
            next=current.next
            current.next=prev
            prev=current
            current=next
            i+=1
            
        if left_node_1 is not None:
            left_node_1.next=prev
        else:
            head=prev
            
        left_node.next=current
        
        return head
        
        