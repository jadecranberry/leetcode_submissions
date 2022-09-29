


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right:
            return head
        
        #find the previous node of the starting point: left_node_1 and the starting point: left_node
        prev=None
        current=head
        i=1
        while current is not None and i<left:
            prev=current
            current=current.next
            i+=1 
        left_node_1=prev
        left_node=current
        
        #reverse the subset of nodes
        i=0
        while current is not None and i<right-left+1:
            next=current.next
            current.next=prev
            prev=current
            current=next
            i+=1
        
        #connect both sides with the reversed subset.
        if left_node_1 is not None:
            left_node_1.next=prev
        else:
            head=prev
            
        left_node.next=current
        
        return head
        
        