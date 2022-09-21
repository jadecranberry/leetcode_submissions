class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        left=0
        word_frequency = {}
        word_length = len(words[0])
        count_words = len(words)
        matched=0
        index_list = []
        
        for word in words:
            if word not in word_frequency:
                word_frequency[word]=0
            word_frequency[word]+=1
        
        #i is the start point of the sliding window, we move it from 0 for the point where the last substring's length is word_length*count_words
        for i in range(len(s)-word_length*count_words+1):
            word_seen = {}
            for j in range(0, count_words):
                next_word_index = i+j*word_length
                word = s[next_word_index:next_word_index+word_length]
                if word not in word_frequency:
                    break
                if word not in word_seen:
                    word_seen[word]=0
                word_seen[word]+=1
                #in get(word, 0), 0 is the default value returned when word not found
                if word_seen[word]>word_frequency.get(word, 0):
                    break
                    
                if j+1==count_words:
                    index_list.append(i)
                
        return index_list         
                
                 