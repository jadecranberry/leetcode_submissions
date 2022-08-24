class Solution:
    def reverseBits(self, n: int) -> int:
        #use ret to accumulate the shifted bits for each bit. Set the initial power to be 31 which is the number to shift the last bit of n
        ret, power = 0, 31
        while(n!=0):
            #n&1 gets the last bit of n.
            #eg. if we shift 1 to left by power 3, we get 1000
            ret += (n&1) << power
            #when we shift the second rightmost bit, the power should be decreased by 1
            power -= 1
            #we shift n to the right by 1 so that we can get the second rightmost by shifting its postion to the last. e.g. 1011 after shifting would be 0101.
            n= n >> 1
        return ret    
    
    