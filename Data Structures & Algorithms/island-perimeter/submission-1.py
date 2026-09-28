class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        p = 0

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    p += 4
                    for x, y in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                        if (0 <= i + x < r) and (0 <= j + y < c) and grid[i + x][j + y] == -1:
                            p -= 2
                    grid[i][j] = -1
        return p
