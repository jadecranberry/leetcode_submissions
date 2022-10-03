# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result=[]
        if root is None:
            return result
        
        queue=deque()
        queue.append(root)
        
        while queue:
            currentLength=len(queue)
            currentSum=0.0
            for _ in range(currentLength):
                currentNode=queue.popleft()
                currentSum+=currentNode.val
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            currentAve=currentSum/currentLength
            result.append(currentAve)
        return result     
            
            