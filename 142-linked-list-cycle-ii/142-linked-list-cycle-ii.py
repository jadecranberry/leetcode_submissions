# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#use fast and slow pointers: 
#1. determine if the list has cycle, if so, we calculate the cycle
#length K with function:calculate_cycle_length. 
#2. then we use two pointers p1 and p2 and advance p2 by the length of K. 
#then we increase them by 1 on each iteration. when p1 and p2 meet, we found the cycle start point
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
            