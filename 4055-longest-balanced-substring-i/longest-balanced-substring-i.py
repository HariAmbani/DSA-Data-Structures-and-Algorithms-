class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 1

        for i in range(n):
            freq = [0] * 26

            for j in range(i, n):
                idx = ord(s[j]) - ord('a')
                freq[idx] += 1

                # Collect all non-zero frequencies
                counts = []
                for x in freq:
                    if x > 0:
                        counts.append(x)

                # Balanced condition: all counts equal
                if len(set(counts)) == 1:
                    ans = max(ans, j - i + 1)

        return ans
