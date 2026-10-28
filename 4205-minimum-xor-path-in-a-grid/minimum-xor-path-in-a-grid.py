class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[[False] * 1024 for _ in range(m)] for _ in range(n)]
        dp[0][0][grid[0][0]] = True

        for i in range(n):
            for j in range(m):
                for k in range(1024):
                    if not dp[i][j][k]:
                        continue

                    if j + 1 < m:
                        dp[i][j + 1][k ^ grid[i][j + 1]] = True

                    if i + 1 < n:
                        dp[i + 1][j][k ^ grid[i + 1][j]] = True

        for k in range(1024):
            if dp[n - 1][m - 1][k]:
                return k

        return -1
        