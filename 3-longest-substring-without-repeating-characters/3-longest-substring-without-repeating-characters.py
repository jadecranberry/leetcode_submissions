#sliding window and use hashmap to store the index of the letters. Once repetitive letter is found, move the start point to the right of the index for the first appearance of the repetitive letter.
class Solution:
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

            