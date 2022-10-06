# Definition for a binary tree node.
# class TreeNode:


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n<=0:
            return []
        return self.generateTreesRecursive(1, n)
    
    def generateTreesRecursive(self, start, end):
        result=[]
        if start>end:
            result.append(None)
            return result
        
        for i in range(start, end+1):
            leftSubtrees = self.generateTreesRecursive(start, i-1)
            rightSubtrees = self.generateTreesRecursive(i+1, end)
            for leftTree in leftSubtrees:
                for rightTree in rightSubtrees:
                    root = TreeNode(i)
                    root.left = leftTree
                    root.right = rightTree
                    result.append(root)
        return result            