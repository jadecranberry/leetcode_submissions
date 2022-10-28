from heapq import *
import heapq

class Solution(object):
    def __init__(self):
        self.maxheap=[]
        self.minheap=[]
        
    def medianSlidingWindow(self, nums, k):
        result=[0.0 for x in range(len(nums)-k+1)]
        for i in range(0, len(nums)):
            if not self.maxheap or -self.maxheap[0]>=nums[i]:
                heappush(self.maxheap, -nums[i])
            else:
                heappush(self.minheap, nums[i])
            self.rebalance_heaps() 
            
            if i-k+1>=0:
                if len(self.maxheap)==len(self.minheap):
                    result[i-k+1]=-self.maxheap[0]/2.0+self.minheap[0]/2.0
                else:
                    result[i-k+1]=-self.maxheap[0]/1.0
                elementToBeRemoved=nums[i-k+1]
                if elementToBeRemoved <= -self.maxheap[0]:
                    self.remove(self.maxheap, -elementToBeRemoved)
                else:
                    self.remove(self.minheap, elementToBeRemoved)
                self.rebalance_heaps()
        return result
    
    def remove(self, heap, element):
        ind = heap.index(element)
        heap[ind] = heap[-1]
        del heap[-1]
        if ind<len(heap):
            heapq._siftup(heap, ind)
            heapq._siftdown(heap, 0, ind)
            
    def rebalance_heaps(self):
        if len(self.maxheap)>len(self.minheap)+1:
            heappush(self.minheap, -heappop(self.maxheap))
        elif len(self.maxheap)<len(self.minheap):
            heappush(self.maxheap, -heappop(self.minheap))
   # def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        