class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        permutations=[]
        permutations.append(s)
        
        for i in range(len(s)):
            if s[i].isalpha():
                for j in range(len(permutations)):
                    chrs = list(permutations[j])
                    chrs[i]=chrs[i].swapcase()
                    permutations.append(''.join(chrs))
                    
        return permutations            
                    