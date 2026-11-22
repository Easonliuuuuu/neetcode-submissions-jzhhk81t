class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        res = 0

        def traverse(i, j):
            if grid[i][j] == 0:
                return 0
            grid[i][j] = 2
            area = 1
            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nxt_i, nxt_j = i + x, j + y
                if 0 <= nxt_i < n and 0 <= nxt_j < m and grid[nxt_i][nxt_j] == 1:
                    area += traverse(nxt_i, nxt_j)
            return area




        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    area = traverse(i, j)
                    res = max(res, area)
        return res
