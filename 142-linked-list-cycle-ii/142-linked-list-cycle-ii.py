# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        K=0
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                K=self.calculate_cycle_length(K, slow)
                break
        
        if K==0:
            return None
        else:
            p1=head
            p2=head
            while K>0:
                p2=p2.next
                K-=1
            while p1!=p2:
                p1=p1.next
                p2=p2.next
            return p1
        
    def calculate_cycle_length(self, k, pointer):
        current = pointer
        while True:
            current=current.next
            k+=1
            if current==pointer:
                break
        return k       
            