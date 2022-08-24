#algorithm:sliding window, two pointers. TC:O(n), SC:O(1)
#start from the first index and calculate the sum of its subarrays until the sum is bigger than the target. At this point, there is no need to continue the subarray with this index. Hence, we need to move the index to the next one and calculate the subarray again.
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #initialize the min_length. It could be infinity or any number that's bigger than the length of nums
        min_length = len(nums) + 1
        left = 0
        total = 0
        #start making subarrays from index 0
        for right, value in enumerate(nums):
            total += value
            while total>= target:
                min_length = min(min_length, right-left+1) 
                total -= nums[left]
                left += 1     
        return min_length if min_length<=len(nums) else 0   
            