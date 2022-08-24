class Solution:
    #sliding window optimized solution
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [None]*128
        left = right = 0
        
        res = 0
        while right<len(s):
            r = s[right]
            #use hashmap to store the index of a letter
            index = chars[ord(r)]
            #check if the index of this letter already in chars, if yes, start new search begining on index+1
            if index != None and index >= left and index<right:
                left = index+1
                
            res = max(res, right-left+1)
            
            chars[ord(r)]=right
            right += 1
        return res    