from collections import deque

class Solution(object):
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        
        dirs = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }
        
        visited = set()
        q = deque([(0, 0)])
        visited.add((0, 0))
        
        while q:
            r, c = q.popleft()
            
            if (r, c) == (m - 1, n - 1):
                return True
            
            for dr, dc in dirs[grid[r][c]]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    
                    # Check reverse direction exists
                    if (-dr, -dc) in dirs[grid[nr][nc]]:
                        visited.add((nr, nc))
                        q.append((nr, nc))
        
        return False