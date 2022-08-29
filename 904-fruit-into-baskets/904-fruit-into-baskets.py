#same as Longest Substring with K Distinct Characters (medium): LC 340
#use sliding window+hashmap
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        max_fruit = 0
        hash = {}
        for right, value in enumerate(fruits):
            if value not in hash:
                hash[value]=0
            hash[value]+=1
 
            while len(hash)>2:
                hash[fruits[left]]-=1
                if hash[fruits[left]]==0:
                    del hash[fruits[left]]
                left+=1
                
            max_fruit = max(max_fruit, right-left+1)    
        return max_fruit         
        