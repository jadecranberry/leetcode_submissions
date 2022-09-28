#fast and slow pointers
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #the following finds the itersection points for slow and fast pointers
        #it should be noted the intersection point is not the cycle entrance point
        slow=fast=nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow==fast:
                break
        
        #the following finds the cycle entrance point by starting the slow point at the begining 
        #and slow down the fast point, when they meet again it is the cycle entrance
        slow = nums[0]
        while slow!=fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return fast    