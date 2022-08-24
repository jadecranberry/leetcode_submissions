#this is basically to search for the totation index in problem 33
class Solution:
    def findMin(self, nums: List[int]) -> int:
        #if the first element is smaller than the last element, the rotated array is the same as the original
        left, right = 0, len(nums)-1
        if nums[left]<nums[right] or len(nums)==1:
            return nums[0]
        
        while left<=right:
            pivot = (left+right)//2
            if nums[pivot]>nums[pivot+1]:
                return nums[pivot+1]
            if nums[pivot-1]>nums[pivot]:
                return nums[pivot]
            if nums[pivot]>nums[0]:
                    left = pivot+1
            else:
                    right = pivot-1
            