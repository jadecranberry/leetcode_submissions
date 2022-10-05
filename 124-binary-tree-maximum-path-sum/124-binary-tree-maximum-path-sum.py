# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.globalMax=-float('inf')
        self.maxPathSum_recursive(root)
        return self.globalMax
    
    def maxPathSum_recursive(self, currentNode):
        if currentNode is None:
            return 0
        
        maxLeftSum=self.maxPathSum_recursive(currentNode.left)
        maxRightSum=self.maxPathSum_recursive(currentNode.right)
        
        maxLeftSum=max(maxLeftSum,0)
        maxRightSum=max(maxRightSum,0)
        
        currentMaxSum=maxLeftSum+maxRightSum+currentNode.val
        
        self.globalMax=max(self.globalMax, currentMaxSum)
        
        return max(maxLeftSum, maxRightSum)+currentNode.val