from heapq import *
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        maxEndHeap=[]
        maxStartHeap=[]
        result = [0]*n
        
        for i in range(n):
            heappush(maxStartHeap, (-intervals[i][0], i) )
            heappush(maxEndHeap, (-intervals[i][1], i))
            
        for _ in range(n):
            topEnd, endIndex = heappop(maxEndHeap)
            result[endIndex]=-1
            
            if -maxStartHeap[0][0] >= -topEnd:
                topStart, startIndex = heappop(maxStartHeap)
                while maxStartHeap and -maxStartHeap[0][0]>= -topEnd:
                    topStart, startIndex = heappop(maxStartHeap)
                result[endIndex] = startIndex    
                heappush(maxStartHeap, (topStart, startIndex))
        return result         