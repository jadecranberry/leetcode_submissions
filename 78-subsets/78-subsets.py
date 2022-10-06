#time complexity: N*2^N, space complexity:N*2^N
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        result.append([])
        for num in nums:
            n=len(result)
            for i in range(n):
                pre_subset_i=list(result[i])
                pre_subset_i.append(num)
                result.append(pre_subset_i)
        return result        