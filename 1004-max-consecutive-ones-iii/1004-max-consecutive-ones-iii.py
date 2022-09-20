

#we don't need hash map to store the frequencies of letters since we only have 1 and 0.
class Solution(object):
    def longestOnes(self, nums, k):
        left, maxlength, max_ones_count=0, 0, 0
        n=len(nums)
        
        for right in range(n):
            if nums[right]==1:
                max_ones_count += 1
            if (right-left+1-max_ones_count)>k:
                if nums[left]==1:
                    max_ones_count -= 1
                left+=1
            maxlength = max(maxlength, right-left+1)
        
        return maxlength