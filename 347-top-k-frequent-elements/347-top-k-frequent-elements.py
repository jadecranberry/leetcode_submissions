#heapq.nlargest(n, iterable, key=None)
#Return a list with the n largest elements from the dataset defined by iterable. key, if provided, specifies a function of one argument that is used to extract a comparison key from each element in iterable

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k==len(nums):
            return nums
        
        count=Counter(nums)
        
        return heapq.nlargest(k, count.keys(), key=count.get)
