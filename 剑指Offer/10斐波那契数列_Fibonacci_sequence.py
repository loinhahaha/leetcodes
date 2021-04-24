# Return Nth number in fibonacci sequence.
# Input: n = 5
# Output: 5  # [0,1,1,2,3,5]
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), N > 1.
# Tip1: Use a, b = b, a+b like in bubble sort.
# Tip2: Return ans % 1000000007 (1 eight zeros 7 )(a prime number)

class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1

        for _ in range(n):
            a, b = b, a+b
        return a % 1000000007
      
