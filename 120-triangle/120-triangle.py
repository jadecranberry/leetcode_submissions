class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        
        pre_row = triangle[0]

        for row in range(1, n):
            curr_row = []
            for col in range(row+1):
                smallest_above = math.inf
                #includes the case when col=row
                if col>0:
                    smallest_above = pre_row[col-1]
                #includes the case when col = 0    
                if col<row:
                    smallest_above = min(smallest_above, pre_row[col])
                curr_row.append(triangle[row][col]+smallest_above)    
            pre_row = curr_row    
            
        return min(pre_row)    
            
        