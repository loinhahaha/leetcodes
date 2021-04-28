# A robot can only walk to (x,y) where x1+x2+y1+y2 <=k in a 2D matrix. (1<=x,y<=100  0<=k<=20)
# Tip: Draw a map, https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/solution/mian-shi-ti-13-ji-qi-ren-de-yun-dong-fan-wei-dfs-b/

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:

        def dfs(i,j,si,sj):
            if i >= m or j >= n or k < si + sj or (i, j) in visited: return 0
            visited.add((i,j))
            return 1 + dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj) + dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)
            # (x+1)⊙10=0 时： sx+1 = sx - 8, example: 19 -> 20  1+9-2-0 = 8 

        visited = set()

        return dfs(0,0,0,0)
