class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i=0
        while i<len(nums):
            j=nums[i]-1
            if nums[i]==nums[j] and i!=j:
                return nums[i]
            if nums[i]!=nums[j]:
                nums[i],nums[j]=nums[j],nums[i]
            else:
                i+=1