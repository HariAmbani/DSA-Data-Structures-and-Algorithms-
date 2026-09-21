class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0

        for i in range(len(s)): 
            ans += (i+1)*(ord('z')-ord(s[i])+1)
        
        return ans
        