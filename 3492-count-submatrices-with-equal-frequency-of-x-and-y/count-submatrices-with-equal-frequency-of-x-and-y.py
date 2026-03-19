class Solution(object):
    def numberOfSubmatrices(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        px = [[0]*cols for _ in range(rows)]
        py = [[0]*cols for _ in range(rows)]

        ans = 0

        for i in range(rows):
            for j in range(cols):
                x = 1 if grid[i][j] == 'X' else 0
                y = 1 if grid[i][j] == 'Y' else 0

                px[i][j] = x
                py[i][j] = y

                if i > 0:
                    px[i][j] += px[i-1][j]
                    py[i][j] += py[i-1][j]
                if j > 0:
                    px[i][j] += px[i][j-1]
                    py[i][j] += py[i][j-1]
                if i > 0 and j > 0:
                    px[i][j] -= px[i-1][j-1]
                    py[i][j] -= py[i-1][j-1]

                # check condition
                if px[i][j] > 0 and px[i][j] == py[i][j]:
                    ans += 1

        return ans