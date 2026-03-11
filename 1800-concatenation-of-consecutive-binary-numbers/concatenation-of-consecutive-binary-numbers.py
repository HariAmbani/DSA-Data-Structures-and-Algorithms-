class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = ""

        for i in range(1, n+1):
            binary = bin(i)
            ans += binary[2:]
        
        return (int(ans, 2) % (pow(10,9) + 7))
        