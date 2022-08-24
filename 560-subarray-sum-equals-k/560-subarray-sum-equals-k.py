class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        presum = 0
        d = {0:1}
        for num in nums:
            presum += num
            if presum - k in d:
                count += d[presum-k]
            if presum not in d:
                d[presum] = 1
            else:
                d[presum] += 1
        return count        