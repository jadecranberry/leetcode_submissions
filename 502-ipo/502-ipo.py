#use two heaps
from heapq import *
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        #use min heap to store the capitals, use max heap to store the profits
        minCapitalHeap = []
        maxProfitHeap = []
        
        #populate the min heap
        for i in range(len(capital)):
            heappush(minCapitalHeap, (capital[i], i))
            
        availableCapital = w
        #since we can only choose k projects.
        for _ in range(k):
            #populate the max heap with all the possible projects we can choose with the availabelCapital
            while minCapitalHeap and minCapitalHeap[0][0]<=availableCapital:
                captial, i = heappop(minCapitalHeap)
                heappush(maxProfitHeap, (-profits[i], i))
            #break if we can't find any project with the avaialble capital    
            if not maxProfitHeap:
                break
                
            availableCapital+=-heappop(maxProfitHeap)[0]    
            
        return availableCapital    