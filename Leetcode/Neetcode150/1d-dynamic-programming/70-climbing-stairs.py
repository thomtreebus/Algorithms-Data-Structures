class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        
        minus_2 = 1
        minus_1 = 2

        for i in range(2, n):
            temp = minus_2
            minus_2 = minus_1
            minus_1 = temp + minus_1
            
        return minus_1