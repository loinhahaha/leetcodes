# Count 1 in a binary number.
# Tip: n & (n-1) -> rightmost 1 to 0
# n: 1011 0000  n-1: 1010 1111  n & (n-1):  1010 0000

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res
# TC: O(N): log_2 n 
# SC: O(1): res

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res
# TC: O(M): M times
# SC: O(1): res

https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/solution/mian-shi-ti-15-er-jin-zhi-zhong-1de-ge-shu-wei-yun/
