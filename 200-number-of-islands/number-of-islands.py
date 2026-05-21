from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        directions = ((0,1), (0,-1), (1,0), (-1,0))
        visited = set()

        def dfs(i,j):
            visited.add((i,j))
            for nr, nc in directions:
                r,c = i+nr, j+nc
                if 0<=r<rows and 0<=c<cols and grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
            

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    islands += 1
        
        return islands


        