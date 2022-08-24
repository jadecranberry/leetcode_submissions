#l:the number of items that are bigger than A[i] on the left side
#r:the number of items that are bigger than A[i] on the right side
#then
#the sum of the subarrays with A[i] as the minimum = A[i](l+1)(r+1)
#use two monotonic stack on both sides of A[i] to find l+1 and r+1
class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        kMod=10**9+7
        n=len(A)
        s, left, right=[], [1]*n, [1]*n
        for i in range(n):
            while s and s[-1][0]>A[i]:
                left[i]+=s.pop()[1]
            s.append((A[i],left[i]))   
        s=[]
        for i in range(n-1, -1, -1):
            while s and s[-1][0]>=A[i]:
                right[i]+=s.pop()[1]
            s.append((A[i],right[i]))
        ans = sum(a*l*r for a,l, r in zip(A, left, right))%kMod
        return ans  