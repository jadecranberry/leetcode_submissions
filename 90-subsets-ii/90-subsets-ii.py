class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #sort nums so that the duplicates are next to each other
        nums.sort()
        result=[]
        result.append([])
        startIndex, endIndex=0,0
        for i in range(len(nums)):
            startIndex=0  
            if i>0 and nums[i]==nums[i-1]:
                #the following endIndex is still the previous subsets endIndex
                startIndex=endIndex+1
            #the following endIndex is the updated one with new subsets added    
            endIndex=len(result)-1    
            for j in range(startIndex, endIndex+1):
                    pre_subset=list(result[j])
                    pre_subset.append(nums[i])
                    result.append(pre_subset)
             
        return result         
                    
                    
                
        