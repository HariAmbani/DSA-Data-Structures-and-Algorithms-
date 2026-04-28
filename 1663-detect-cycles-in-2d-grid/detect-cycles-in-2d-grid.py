class Solution(object):
    def containsCycle(self, grid):
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(r,c,pr,cr):
            visited.add((r,c))

            for dr,dc in directions:
                nr, nc = r+dr, c+dc

                if((0 <= nr < rows) and (0 <= nc < cols) and grid[nr][nc] == grid[r][c]):
                    if (nr, nc) not in visited:
                        if dfs(nr, nc, r, c):
                            return True
                    elif nr != pr and nc != cr:
                            return True
            
            return False
        

        for i in range(rows):
            for j in range(cols):
                if ((i,j) not in visited):
                    if dfs(i,j,-1,-1):
                        return True

        return False