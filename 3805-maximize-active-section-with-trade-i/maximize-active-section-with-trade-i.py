class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        totalOnes = 0

        prevZero = float("-inf")
        bestGain = 0

        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1

            length = j - i

            if s[i] == '1':
                totalOnes += length
            else:
                bestGain = max(bestGain, prevZero + length)
                prevZero = length

            i = j

        return totalOnes + bestGain