class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, curr = 0, 0
        p2=len(nums)-1
        
        while curr<=p2:
            if nums[curr]==0:
                nums[p0], nums[curr]=nums[curr], nums[p0]
                p0+=1
                curr+=1
            elif nums[curr]==2:
                nums[p2], nums[curr]=nums[curr],nums[p2]
                p2-=1
                #at this time we don't want to increase curr cause we also need to compare the swapped value in the next round
            else:
                curr+=1