class Solution:
    def climbStairs(self, n: int) -> int:
        #fibonichi series
        first = 0
        second = 1
        fibo = 0

        if n<=1:
            return n
        else:
            for _ in range(n):
                fibo = first + second
                first = second
                second = fibo
        return fibo        
                 
