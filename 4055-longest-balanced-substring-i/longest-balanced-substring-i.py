class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        n = len(s)
        ans = 0
        maxi = 0

        i = 0
        while i < n and ans < n-i:
            freq = {}
            maxi = 1
            for j in range(i, n):
                if s[j] not in freq:
                    freq[s[j]] = 1
                else:
                    freq[s[j]] += 1
                    maxi = max(maxi, freq[s[j]])
                if freq[s[j]] == maxi:
                    if (len(set(freq.values()))==1):
                        ans = max(ans, j-i+1)
            i += 1
        return ans
