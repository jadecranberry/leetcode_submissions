class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left = 0
        char_frequency = {}
        min_length = len(s)+1
        match = 0
        
        for char in t:
            if char not in char_frequency:
                char_frequency[char]=0
            char_frequency[char]+=1
        
        for right, value in enumerate(s):
            if value in char_frequency:
                char_frequency[value]-=1
                if char_frequency[value]==0:
                    match+=1
            while match==len(char_frequency):
                if min_length>right-left+1:
                    min_length=right-left+1
                    substr_start=left
                
                left_char=s[left]
                left += 1
                if left_char in char_frequency:
                    if char_frequency[left_char]==0:
                        match-=1
                    char_frequency[left_char]+=1    
                    
        if min_length>len(s):
            return ""
        return s[substr_start:substr_start+min_length]     
                    