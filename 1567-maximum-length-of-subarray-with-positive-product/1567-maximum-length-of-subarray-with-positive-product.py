class Solution:
    #Define two counters pos and neg as the length of positive and negative products ending at current element.
    def getMaxLen(self, nums: List[int]) -> int:
        ans = pos = neg = 0
        for x in nums: 
            if x > 0: 
                # for neg, if the previous neg>0, neg[i]=neg[i-1]+1, else neg[i]=0
                pos, neg = 1 + pos, 1 + neg if neg else 0
            elif x < 0: 
                #for pos, if we have previous neg then the product we be positive, we use the amount of negatives to figure the length of positive. Otherwise the array was reset to zero. 
                pos, neg = 1 + neg if neg else 0, 1 + pos
            else: 
                pos = neg = 0 # reset 
            ans = max(ans, pos)
        return ans 
  
            
        