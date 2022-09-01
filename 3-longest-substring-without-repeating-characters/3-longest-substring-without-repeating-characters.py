class Solution:
    #sliding window optimized solution
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxlength = 0            
        hash = {}
        
        for right, value in enumerate(s):
            if value in hash:
                left = max(left, hash[value] + 1)
            hash[value]=right
            maxlength=max(maxlength, right-left+1)
           
        return maxlength  

            