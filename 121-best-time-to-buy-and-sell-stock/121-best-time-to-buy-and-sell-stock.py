class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        imin, res = float('inf'),0
        for p in prices:
            imin = min(imin, p)
            res = max(res, p-imin)
        if res<0:
            return 0
        return res
        