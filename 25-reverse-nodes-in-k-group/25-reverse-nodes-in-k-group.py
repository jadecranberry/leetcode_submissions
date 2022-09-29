
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k<=1 or head is None:
            return head
        
        cur=head
        prev=None
        while True:
            last_node_of_previous_part=prev
            last_node_of_sublist=cur
            i=0
            
            count=0
            p=cur
            while p and count<k:
                p=p.next
                count+=1
            
            if count==k:
                while cur is not None and i<k:
                    Next=cur.next
                    cur.next=prev
                    prev=cur
                    cur=Next
                    i+=1
                    
                if last_node_of_previous_part is not None:
                    last_node_of_previous_part.next=prev
                else:
                    head=prev
                
                last_node_of_sublist.next=cur  
                prev=last_node_of_sublist
            else:
                return head
                  
                
                