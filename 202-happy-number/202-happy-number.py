class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, n
        while True:
            slow = self.find_square_sum(slow)
            fast = self.find_square_sum(self.find_square_sum(fast))
            if slow == fast:
                break
        return slow==1         
            
            
    def find_square_sum(self, n):
        _sum=0
        while n>0:
            digit=n%10
            _sum+=digit*digit
            n//=10
        return _sum     