from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        directions = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [-1,-1], [1,-1], [-1,1]]
        visited = set()

        if n == 1:
            if grid[0][0] == 0:
                return 1
            else:
                return -1
            
        if grid[0][0] == 1 or grid[len(grid)-1][len(grid)-1] == 1:
            return -1

        q = deque([(0,0,1)])
        #visited.add((0,0))
        grid[0][0] = 1 #making grid[i][j]=1 to use it as visited instead of seperate set

        while q:
            row, col, dis = q.popleft()
            for i,j in directions:
                r,c = row+i, col+j
                if (0 <= r < n) and (0 <= c < n) and (r,c) not in visited and grid[r][c] == 0:
                    if r == n-1 and c == n-1:
                        return dis+1
                    q.append((r,c,dis+1))
                    grid[r][c] =1
                    
        return -1


        