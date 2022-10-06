

from collections import deque
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        wordLen=len(word)
        result=[]
        queue=deque()
        queue.append(abbreviatedWord(list(), 0, 0))
        while queue:
            abWord = queue.popleft()
            if abWord.start == wordLen:
                if abWord.count != 0:
                    abWord.str.append(str(abWord.count))
                result.append(''.join(abWord.str))
            else:
                #abbreviate the current character
                queue.append(abbreviatedWord(list(abWord.str), abWord.start+1, abWord.count+1))
                if abWord.count != 0:
                    abWord.str.append(str(abWord.count))
                #skip the current character    
                newWord = list(abWord.str)
                newWord.append(word[abWord.start])
                queue.append(abbreviatedWord(newWord, abWord.start+1, 0))
        return result        
        
class abbreviatedWord:        
    def __init__(self, str, start, count):
        self.str=str
        self.start=start
        self.count=count