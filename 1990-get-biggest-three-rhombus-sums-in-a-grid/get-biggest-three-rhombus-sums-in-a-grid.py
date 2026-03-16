class Solution(object):
    def getBiggestThree(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        
        res = set()
        
        for i in range(rows):
            for j in range(cols):
                
                # size = 0 rhombus (single cell)
                res.add(grid[i][j])
                
                size = 1
                while True:
                    
                    if i + 2*size >= rows or j - size < 0 or j + size >= cols:
                        break
                    
                    total = 0
                    
                    # top -> left
                    for k in range(size):
                        total += grid[i+k][j-k]
                    
                    # left -> bottom
                    for k in range(size):
                        total += grid[i+size+k][j-size+k]
                    
                    # bottom -> right
                    for k in range(size):
                        total += grid[i+2*size-k][j+k]
                    
                    # right -> top
                    for k in range(size):
                        total += grid[i+size-k][j+size-k]
                    
                    res.add(total)
                    
                    size += 1
        
        return sorted(res, reverse=True)[:3]