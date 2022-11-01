class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        # Ways to get here.
        prev = 1
        curr = 2
        
        for ii in range(3, n + 1):
            temp = prev + curr
            prev = curr
            curr = temp
            
        return curr
