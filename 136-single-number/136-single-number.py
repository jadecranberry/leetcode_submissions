class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=0
        # a xor 0 xor a  =  a xor a  =0
        for i in nums:
            a ^= i
        return a  

    
        