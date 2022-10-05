from heapq import *
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minCapitalHeap = []
        maxProfitHeap = []
        
        for i in range(len(capital)):
            heappush(minCapitalHeap, (capital[i], i))
            
        availableCapital = w
        for _ in range(k):
            while minCapitalHeap and minCapitalHeap[0][0]<=availableCapital:
                captial, i = heappop(minCapitalHeap)
                heappush(maxProfitHeap, (-profits[i], i))
                
            if not maxProfitHeap:
                break
                
            availableCapital+=-heappop(maxProfitHeap)[0]    
            
        return availableCapital    