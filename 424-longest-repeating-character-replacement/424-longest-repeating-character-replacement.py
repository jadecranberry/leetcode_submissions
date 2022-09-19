class Solution(object):


    def characterReplacement(self, s, k):
        left, max_length, max_repeat_letter_count = 0, 0, 0
        frequency_map={}
        
        for right in range(len(s)):
            right_char = s[right]
            if right_char not in frequency_map:
                frequency_map[right_char]=0
            frequency_map[right_char]+=1
            
            max_repeat_letter_count = max(max_repeat_letter_count, frequency_map[right_char])
            if (right-left+1-max_repeat_letter_count)>k:
                left_char=s[left]
                frequency_map[left_char]-=1
                left+=1
            max_length = max(max_length, right-left+1)
        return max_length        
        
        
        