class Solution(object):
    def countSubmatrices(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        prev_row = [0]*cols
        ans = 0

        if grid[0][0] > k:
            return 0
        
        col_limit = cols

        for i in range(rows):
            cur_area = 0
            j = 0
            while j < col_limit:
                if cur_area+grid[i][j]+prev_row[j] <= k:
                    ans += 1
                    grid[i][j] += prev_row[j]
                    cur_area = cur_area + grid[i][j]
                    j += 1
                else:
                    col_limit = j
                    break
            prev_row = grid[i]
    
        return ans




        