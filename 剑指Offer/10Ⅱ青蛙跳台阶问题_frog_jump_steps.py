# A frog can jump up 1 setp or 2 steps.
# How many solutions for it to jump up n steps.

# Tip: From top to bottom f(n) = f(n-1) + f(n-2) and f(2) = f(1)+f(0) so f(0) = 1 f(1) = 1 
# Use fibonacci sequence.

class Solution:
    def numWays(self, n: int) -> int:
        
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a+b
        return(a%1000000007)
      
