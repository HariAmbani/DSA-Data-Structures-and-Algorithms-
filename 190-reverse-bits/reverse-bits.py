class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        rever = ""
        for _ in range(32):
            if n&1 == 1:
                rever += "1"
            else:
                rever += "0"
            n = n >> 1
        ans = 0
        for i in range(len(rever)):
            if rever[i] == "1":
                ans += pow(2, len(rever)-i-1)
        return ans


        