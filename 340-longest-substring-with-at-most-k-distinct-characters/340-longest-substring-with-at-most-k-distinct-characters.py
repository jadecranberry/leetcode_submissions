#sliding window + hashmap
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        hashmap = defaultdict()
        n = len(s)
        if n*k==0:
            return 0
        
        left, right = 0, 0
        max_length = 0
        
        for right in range(n):
            if s[right] not in hashmap:
                hashmap[s[right]]=0
            hashmap[s[right]]+=1
            while len(hashmap) > k:
                hashmap[s[left]]-=1
                if hashmap[s[left]]==0:
                    del hashmap[s[left]]
                left+=1
            max_length = max(max_length, right-left+1)  
        return max_length     