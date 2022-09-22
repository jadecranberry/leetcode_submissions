class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count=0
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                sums = nums[i]+nums[l]+nums[r]
                if sums>=target:
                    r-=1
                if sums<target:
                    count+=r-l
                    l+=1
        return count            