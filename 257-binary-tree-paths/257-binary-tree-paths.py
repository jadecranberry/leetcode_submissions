# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        allPaths=[]
        if root is None:
            return
        self.binaryTreePath_recursive(root, '', allPaths)
        return allPaths
        
    def binaryTreePath_recursive(self, currentNode, currentPath, allPaths):
        if currentNode is None:
            return
        currentPath+=str(currentNode.val)
        
        if currentNode.left is None and currentNode.right is None:
            allPaths.append(currentPath)
        else:
            currentPath+='->'
            self.binaryTreePath_recursive(currentNode.left, currentPath, allPaths)
            self.binaryTreePath_recursive(currentNode.right, currentPath, allPaths)
        #since there is no backtracking, we don't need to delete the last element in currentPath   
          
            