class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = []

        cur = 1
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                cur += 1
            else:
                count.append(cur)
                cur = 1
        count.append(cur)
        
        ans = 0

        for i in range(1, len(count)):
            ans += min(count[i], count[i-1])
        
        return ans




        