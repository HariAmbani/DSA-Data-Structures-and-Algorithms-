class Solution(object):
    def reverseSubmatrix(self, grid, x, y, k):
        """
        :type grid: List[List[int]]
        :type x: int
        :type y: int
        :type k: int
        :rtype: List[List[int]]
        """
        for i in range(k//2):
            temp = grid[x+i][y:y+k]
            grid[x+i][y:y+k] = grid[x+k-i-1][y:y+k]
            grid[x+k-i-1][y:y+k] = temp
        
        return grid

        