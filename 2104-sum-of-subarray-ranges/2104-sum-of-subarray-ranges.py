#Solution 2, O(n) Stack Solution
class Solution:
    def subArrayRanges(self, A0: List[int]) -> int:
        res=0
        inf=float('inf')
        A=[-inf]+A0+[-inf]#:A=[-inf, A0, -inf]
        s=[]
        for i,x in enumerate(A):
            while s and A[s[-1]]>x:
                j=s.pop()
                k=s[-1]
                res -= A[j]*(i-j)*(j-k)
            s.append(i)   
            
        A = [inf]+A0+[inf]
        s=[]
        for i, x in enumerate(A):
            while s and A[s[-1]]<x:
                j = s.pop()
                k=s[-1]
                res+=A[j]*(i-j)*(j-k)
            s.append(i)
        return res    
