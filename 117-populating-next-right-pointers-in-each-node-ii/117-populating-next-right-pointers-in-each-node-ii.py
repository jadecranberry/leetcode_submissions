"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return
        
        queue=deque()
        queue.append(root)
        while queue:
            currentLength=len(queue)
            preNode=None
            for _ in range(currentLength):
                currentNode=queue.popleft()
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
                if preNode:
                    preNode.next=currentNode
                preNode=currentNode    
        return root        