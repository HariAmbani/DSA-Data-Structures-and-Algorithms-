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
            print("x : ",x)
            print("y : ",y)
            print("k : ",k)
            print("i : ",i)
            print("grid[x][y:y+k] : ", grid[x][y:y+k])
            print("grid[x+k-i-1][y:y+k] : ", grid[x+k-i-1][y:y+k])
            print("---------------")
            temp = grid[x+i][y:y+k]
            grid[x+i][y:y+k] = grid[x+k-i-1][y:y+k]
            grid[x+k-i-1][y:y+k] = temp
        
        return grid

        