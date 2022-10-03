# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=[]
        if root is None:
            return result
        queue=deque()
        queue.append(root)
        while queue:
            current_length=len(queue)
            current_level=[]
            i=0
            for _ in range(current_length):
                current_node=queue.popleft()
                current_level.append(current_node.val)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            result.append(current_level)     
        result=result[::-1]        
        return result      