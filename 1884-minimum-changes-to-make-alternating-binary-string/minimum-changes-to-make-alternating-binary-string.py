class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        valid_one = ""
        valid_two = ""

        cur_one = "1"
        cur_two = "0"

        for i in range(len(s)):
            valid_one += cur_one
            valid_two += cur_two
            if cur_one == "1":
                cur_one = "0"
                cur_two = "1"
            else:
                cur_one = "1"
                cur_two = "0"
        
        ans_one = 0
        ans_two = 0

        for i in range(len(s)):
            if s[i] != valid_one[i]:
                ans_one += 1
            if s[i] != valid_two[i]:
                ans_two += 1
        
        return min(ans_one, ans_two)

        