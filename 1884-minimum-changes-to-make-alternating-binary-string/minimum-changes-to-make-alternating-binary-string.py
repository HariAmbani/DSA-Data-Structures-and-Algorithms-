class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        valid_one = ""

        cur_one = "1"

        for i in range(len(s)):
            valid_one += cur_one
            if cur_one == "1":
                cur_one = "0"
            else:
                cur_one = "1"
        
        ans_one = 0

        for i in range(len(s)):
            if s[i] != valid_one[i]:
                ans_one += 1
        
        return min(ans_one, len(s)-ans_one)

        