# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        if root is None:
            return len(arr)==0
        
        return self.isValidSequence_recursive(root, arr, 0)
    
    def isValidSequence_recursive(self, currentNode, sequence, sequenceIndex):
        if currentNode is None:
            return False
        seqLen=len(sequence)
        if sequenceIndex>=seqLen or currentNode.val!=sequence[sequenceIndex]:
            return False
        
        if currentNode.left is None and currentNode.right is None and sequenceIndex==len(sequence)-1:
            return True
        
        return self.isValidSequence_recursive(currentNode.left, sequence, sequenceIndex+1) or self.isValidSequence_recursive(currentNode.right, sequence, sequenceIndex+1)