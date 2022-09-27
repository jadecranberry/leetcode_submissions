# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#copy all values in linked list to arry vals and then compare the values with the reversed values
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals=[]
        current_node=head
        while current_node:
            vals.append(current_node.val)
            current_node=current_node.next
            #vals[::-1] reverses vals
        return vals==vals[::-1]