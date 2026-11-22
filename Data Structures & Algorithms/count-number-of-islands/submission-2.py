class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])

        def traverse(i, j):
            if grid[i][j] == '0':
                return 
            if grid[i][j] == '1':
                grid[i][j] = '2'
            
            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nxt_i, nxt_j = i + x, j + y
                if 0 <= nxt_i < n and 0 <= nxt_j < m and grid[nxt_i][nxt_j] == '1':
                    traverse(nxt_i, nxt_j)
            return 

        res = 0
        for i in range(n):
            for k in range(m):
                if grid[i][k] == '1':
                    res += 1
                    traverse(i, k)
        return res


        


            