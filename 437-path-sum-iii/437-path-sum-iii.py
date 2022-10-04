# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return self.pathSum_recursive(root, targetSum, [])
    
    def pathSum_recursive(self, currentNode, target, currentPath):
        if currentNode is None:
            return 0
        
        currentPath.append(currentNode.val)
        currentSum=0
        pathCount=0
        # based on the examples, the root value may not be in the list, therefore we sum backwards
        # once we found the sum we found, we add one to the pathCount
        for i in range(len(currentPath)-1, -1, -1):
            currentSum+=currentPath[i]
            if currentSum==target:
                pathCount+=1
            
                
        pathCount+=self.pathSum_recursive(currentNode.left, target, currentPath)
        pathCount+=self.pathSum_recursive(currentNode.right, target, currentPath)
        del currentPath[-1]
        return pathCount
        