class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        decimal = int(s, 2)

        ans = 0
        while decimal != 1:
            ans += 1
            if decimal%2 == 0:
                decimal = int(decimal/2)
            else:
                decimal += 1
        
        return ans


        