class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        prev = 0
        cur = 1

        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                cur += 1
            else:
                ans += min(prev, cur)
                prev = cur
                cur = 1

        ans += min(prev, cur)
        
        return ans




        