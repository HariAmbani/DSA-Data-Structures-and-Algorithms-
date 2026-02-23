class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        one = 1
        two = 1

        for i in range(2, n+1):
            temp = two
            two = one+two
            one = temp
        
        return two
        



        
        