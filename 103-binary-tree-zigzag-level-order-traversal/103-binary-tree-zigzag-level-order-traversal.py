# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=[]
        if root is None:
            return result
        
        queue=deque()
        queue.append(root)
        LeftToRight=True
        while queue:
            currentLength=len(queue)
            currentLevel=deque()
            for _ in range(currentLength):
                    currentNode=queue.popleft()
                    if LeftToRight:
                        currentLevel.append(currentNode.val)
                    else:
                        currentLevel.appendleft(currentNode.val)
                    if currentNode.left:
                        queue.append(currentNode.left)
                    if currentNode.right:
                        queue.append(currentNode.right)
            LeftToRight= not LeftToRight
            result.append(list(currentLevel))
        return result    
                    
                