class Solution(object):
    def canPartitionGrid(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        total_sum = sum(sum(row) for row in grid)

        if total_sum % 2:
            return False
        
        half = total_sum // 2

        # Check row-wise partition
        cur = 0
        for i in range(rows):
            cur += sum(grid[i])
            if cur == half:
                return True

        # Check column-wise partition
        cur = 0
        for j in range(cols):
            col_sum = 0
            for i in range(rows):
                col_sum += grid[i][j]
            cur += col_sum
            if cur == half:
                return True

        return False