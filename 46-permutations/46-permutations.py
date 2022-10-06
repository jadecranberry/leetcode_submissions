#use BFS

from collections import deque
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        numsLength=len(nums)
        result=[]
        permutations = deque()
        permutations.append([])
        for num in nums:
            n=len(permutations)
            for _ in range(n):
                oldpermutation = permutations.popleft()
                for j in range(len(oldpermutation)+1):
                    newPermutation=list(oldpermutation)
                    newPermutation.insert(j, num)
                    if len(newPermutation)==numsLength:
                        result.append(newPermutation)
                    else:
                        permutations.append(newPermutation)
        return result                