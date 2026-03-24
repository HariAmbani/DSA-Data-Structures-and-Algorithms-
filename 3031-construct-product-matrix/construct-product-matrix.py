class Solution(object):
    def constructProductMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        total_product = 1

        rows = len(grid)
        cols = len(grid[0])

        found_count = 0
        found_indexes = []

        for i in range(rows):
            for j in range(cols):
                if (grid[i][j] % 12345) != 0:
                    total_product = (total_product * grid[i][j])
                else:
                    found_count += 1
                    if found_indexes == []:
                        found_indexes.append(i)
                        found_indexes.append(j)

        if found_count == 0:
            for i in range(rows):
                for j in range(cols):
                    grid[i][j]  = (total_product/grid[i][j]) % 12345 
        
        elif found_count == 1:
            for i in range(rows):
                for j in range(cols):
                    if i == found_indexes[0] and j == found_indexes[1]:
                        grid[i][j] = total_product % 12345
                    else:
                        grid[i][j] = 0
        else:
            for i in range(rows):
                for j in range(cols):
                    grid[i][j] = 0           
        
        return grid
        