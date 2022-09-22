#two pointers. similar to leetcode: 16. 3Sum Closest

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
                   # since nums[right] >= nums[left], therefore, we can replace nums[right] by any number between
                   # left and right to get a sum less than the target sum
                    count+=r-l
                    l+=1
        return count            