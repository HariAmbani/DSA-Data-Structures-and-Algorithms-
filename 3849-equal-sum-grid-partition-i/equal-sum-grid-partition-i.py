class Solution(object):
    def canPartitionGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        rows = len(grid)
        cols = len(grid[0])
        total_sum = 0

        rows_sum = []
        cols_sum = []

        for i in range(rows):
            cur_sum = 0
            for j in range(cols):
                cur_sum += grid[i][j]
            rows_sum.append(cur_sum)
            total_sum += cur_sum
        
        if total_sum % 2 == 1:
            return False
        
        half_total = int(total_sum/2)

        cur_sum = 0
        for i in rows_sum:
            cur_sum += i
            if (cur_sum == half_total):
                return True    
                    

        for i in range(cols):
            cur_sum = 0
            for j in range(rows):
                cur_sum += grid[j][i]
            cols_sum.append(cur_sum)

        cur_sum = 0
        for i in cols_sum:
            cur_sum += i
            if (cur_sum == half_total):
                return True
        
        return False

        