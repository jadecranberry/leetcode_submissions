# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        queue=deque()
        queue.append(root)
        minimumDepth = 0
        while queue:
            minimumDepth += 1
            currentLength=len(queue)
            for _ in range(currentLength):
                currentNode = queue.popleft()
                if currentNode.left is None and currentNode.right is None:
                    return minimumDepth
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
        return minimumDepth            