class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #the greedy solution
        #If you can jump to i, then you can jump to atleast i + nums[i].
        #Always jump as far as you can.
        #Keep tracking the farthest index you can jump to.
        
        #the maximum index we can reach so far
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i+n)
        return True
      