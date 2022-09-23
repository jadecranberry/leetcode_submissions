

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        while low<len(nums)-1 and nums[low+1]>=nums[low]:
            low+=1
           
        if low==len(nums)-1:
            return 0
        
        while high>0 and nums[high-1]<=nums[high]:
            high-=1
            
        subarray_min = min(nums[low:high+1])    
        subarray_max = max(nums[low:high+1])
        
        while low>0 and nums[low-1]>subarray_min:
            low-=1
            
        while high<len(nums)-1 and nums[high+1]<subarray_max:
            high+=1
            
        return high-low+1    