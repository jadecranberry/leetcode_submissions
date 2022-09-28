class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i=0
        while i<len(nums):
            j=nums[i]-1
            #if there are repetitive elements, nums[i] might eaqual to nums[j] although i and j is different, hence this condition would skip duplicate elements.
            if nums[i]!=nums[j]:
                nums[i], nums[j]=nums[j],nums[i]
            else:
                i+=1
        output=[] 
        for i in range(len(nums)):
            if nums[i]!=i+1:
                output.append(i+1)
        return output        
        