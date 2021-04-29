# Regular expression mapping
# Input: str s and rules p Output: True or False
# Denote: '.': any letter '*': any times
# Tip: Dynamic programing


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s) + 1, len(p) + 1
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True
        # initialize first line
        for j in range(2, n, 2):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'  # check if the rule match no input
            
        # change state
        for i in range(1, m):
            for j in range(1, n):
                if p[j - 1] == '*':                                               # 
                    if dp[i][j - 2]: dp[i][j] = True                              # 1. zero times
                    elif dp[i - 1][j] and s[i - 1] == p[j - 2]: dp[i][j] = True   # 2. dp[i-1][j] one more time
                    elif dp[i - 1][j] and p[j - 2] == '.': dp[i][j] = True        # 3. one '.'
                else:
                    if dp[i - 1][j - 1] and s[i - 1] == p[j - 1]: dp[i][j] = True # 1. match one letter / one more letter one more rule
                    elif dp[i - 1][j - 1] and p[j - 1] == '.': dp[i][j] = True    # 2. match one '.'
        return dp[-1][-1]
      
# SC: O(MN) traverse state array
# TC: O(MN) state array takes up MN space
'''
https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/solution/jian-zhi-offer-19-zheng-ze-biao-da-shi-pi-pei-dong/
'''
