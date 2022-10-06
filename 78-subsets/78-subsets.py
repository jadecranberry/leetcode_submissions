def find_subsets(nums):
  subsets = []
  # start by adding the empty subset
  subsets.append([])
  for currentNumber in nums:
    # we will take all existing subsets and insert the current number in them to create new subsets
    n = len(subsets)
    for i in range(n):
      # create a new subset from the existing subset and insert the current element to it
      set1 = list(subsets[i])
      set1.append(currentNumber)
      subsets.append(set1)

  return subsets
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