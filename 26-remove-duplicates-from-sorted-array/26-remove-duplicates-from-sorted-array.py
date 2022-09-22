class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        insertindex = 1
        for i in range(1, size):
            if nums[i-1]!=nums[i]:
                nums[insertindex]=nums[i]
                insertindex += 1
            
        return insertindex    