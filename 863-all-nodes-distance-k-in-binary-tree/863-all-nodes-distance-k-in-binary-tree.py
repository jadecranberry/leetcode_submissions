# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #Use dfs to find all parent nodes
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, par=None):
            if node:
                node.par=par
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)
     
    #use bfs to find all nodes that have distance k from target.
        queue=collections.deque([(target,0)])
        seen={target}
        while queue:
            if queue[0][1]==k:
                return [node.val for node, d in queue]
            node, d = queue.popleft()
            for nei in (node.left, node.right, node.par):
            #the following should read as (if nei) and (nei not in seen). This is to exclude null nodes.    
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, d+1))
        return []            
        