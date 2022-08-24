class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        DIR = [0, 1, 0, -1, 0]
        q = deque([])
        #set all the cells to -1 if the value is not 0 and put all the values that equals to 0 into queue
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = -1
        while q:
            r, c =q.popleft()
            #check for all four directions of each cell
            for i in range(4):
                nr, nc = r + DIR[i], c+DIR[i+1]
                if nr<0 or nr == m or nc<0 or nc ==n or mat[nr][nc]!=-1: continue
                #once we find a -1 cell that closest to 0, we change its distance to 1    
                mat[nr][nc] = mat[r][c]+1
                #once we are done changing the value for (nr, nc), we add it to the queue
                q.append((nr,nc))
        return mat     
