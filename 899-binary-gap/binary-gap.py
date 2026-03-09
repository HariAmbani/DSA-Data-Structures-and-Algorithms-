class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """

        ans = 0

        i = 0

        while i < 32:
            if ((n >> i) & 1):
                j = i
                count = 1
                i += 1
                while i < 32 and ((n >> i) & 1) != 1:
                    i += 1
                    count += 1
                if ((n >> i) & 1) == 1:
                    ans = max(ans, i-j)
            else:
                i += 1
        return ans




        