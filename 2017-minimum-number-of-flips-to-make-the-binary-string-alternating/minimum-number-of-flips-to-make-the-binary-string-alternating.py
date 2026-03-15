import heapq
class Solution(object):
    def minFlips(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        s = s+s

        valid = ["0"]

        for i in range(len(s)-1):
            if valid[-1] == "0":
                valid.append("1")
            else:
                valid.append("0")
        
        valid = "".join(valid)
        print(valid)

        ans = float('inf')
        cur = 0
        l = 0
        for r in range(len(s)):
            if s[r] != valid[r]:
                cur += 1
            if r-l+1 > n:
                if s[l] != valid[l]:
                    cur -= 1
                l += 1
            if r-l+1 == n:
                ans = min(ans, cur, n-cur)
        
        return ans
        
        