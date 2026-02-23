class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        fibonacci = [1,1]

        for i in range(2, n+1):
            next_value = fibonacci[0] + fibonacci[1]
            fibonacci[0] = fibonacci[1]
            fibonacci[1] = next_value
        
        return next_value
        



        
        