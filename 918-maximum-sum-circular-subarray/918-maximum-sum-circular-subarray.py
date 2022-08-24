class Solution(object):
    def maxSubarraySumCircular(self, A:List[int]) -> int:        
        def kadane(gen):
            # Maximum non-empty subarray sum
            ans = cur = None
            for i, x in enumerate(gen):
                if i == 0:
                    cur = x
                    ans = x
                else:
                    cur = x + max(cur, 0)           
                ans = max(ans, cur)
            return ans
        
        S = sum(A)
        if len(A) == 1:
            return S
        
        ans1 = kadane(iter(A))
        ans2 = S + kadane(-A[i] for i in range(1, len(A)))
        ans3 = S + kadane(-A[i] for i in range(0, len(A) - 1))
        return max(ans1, ans2, ans3)
        