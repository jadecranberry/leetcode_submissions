#we don't need to return all peaks, just one peak is ok.
#since nums[i] != nums[i + 1] for all valid i, we can treat each section as either increasing or decreasing.
#we always go in the direction of increaseing to find a peak.
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l<r:
            mid = (r+l)//2
            if nums[mid]<nums[mid+1]:
                l = mid+1
            else:
                r = mid
        return l        
                