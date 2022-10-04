# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        allPaths=[]
        self.pathSum_recursive(root, targetSum, [], allPaths)
        return allPaths
    
    def pathSum_recursive(self, currentNode, targetSum, currentPath, allPaths):
        if currentNode is None:
            return
        
        currentPath.append(currentNode.val)
        if currentNode.val==targetSum and currentNode.left is None and currentNode.right is None:
            allPaths.append(list(currentPath))
        else:
            self.pathSum_recursive(currentNode.left, targetSum-currentNode.val, currentPath, allPaths)
            self.pathSum_recursive(currentNode.right, targetSum-currentNode.val, currentPath, allPaths)
        del currentPath[-1]     