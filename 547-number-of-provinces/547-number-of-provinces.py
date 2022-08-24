class Solution:
    def findCircleNum(self, A: List[List[int]]) -> int:
        N=len(A)
        SEEN=set()
        def dfs(node):
            for j, value in enumerate(A[node]):
                if value and j not in SEEN:
                    SEEN.add(j)
                    dfs(j)
        ans = 0
        #treat each A[i] as a node
        for i in range(N):
            if i not in SEEN:
                #use dfs to find all the other nodes that's connected to i and add those nodes to SEEN
                dfs(i)
                ans += 1
        return ans        
