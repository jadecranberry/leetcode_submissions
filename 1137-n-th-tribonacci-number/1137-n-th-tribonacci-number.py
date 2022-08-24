class Solution:
    def tribonacci(self, n: int) -> int:
        if n<=2:
            if n == 2:
                return 1
            else:
                return n
      
        current = 0
        pre1 = 1
        pre2 = 1
        pre3 = 0
        for i in range(3, n+1):
            current = pre1+pre2+pre3
            pre3 = pre2
            pre2 = pre1
            pre1 = current
        return current    