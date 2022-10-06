from collections import deque
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        queue = deque()
        queue.append(ParenthesesString("", 0, 0))
        while queue:
            ps=queue.popleft()
            if ps.openCount==n and ps.closeCount==n:
                result.append(ps.str)
            else:
                if ps.openCount<n:
                    queue.append(ParenthesesString(ps.str+"(", ps.openCount+1, ps.closeCount))
                if ps.openCount>ps.closeCount:
                    queue.append(ParenthesesString(ps.str+")", ps.openCount, ps.closeCount+1))
        return result            
        
class ParenthesesString:    
    def __init__(self, str, openCount, closeCount):
        self.str = str
        self.openCount = openCount
        self.closeCount = closeCount