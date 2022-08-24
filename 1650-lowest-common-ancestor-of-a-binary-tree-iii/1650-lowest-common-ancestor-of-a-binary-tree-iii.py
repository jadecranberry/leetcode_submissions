"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node'):
        A = p
        B = q
        
        while A != B:
            A = q if A is None else A.parent
            B = p if B is None else B.parent
            
        return A    
        