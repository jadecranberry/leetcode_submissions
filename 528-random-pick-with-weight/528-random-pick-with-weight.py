class Solution:

    def __init__(self, w: List[int]):
        self.presums = []
        presum = 0
        for weight in w:
            presum += weight
            self.presums.append(presum)
        self.total_sum = presum

    def pickIndex(self) -> int:
        target = self.total_sum*random.random()
        low, high = 0, len(self.presums)
        while low < high:
            mid = low + (high - low)//2
            if target > self.presums[mid]:
                low = mid+1
            else:
                high = mid
        return low        
                

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()