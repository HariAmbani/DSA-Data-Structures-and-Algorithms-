class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_dict = {}
        start = 0
        max_len = 0
        for i in range(len(s)):
            if s[i] in char_dict and char_dict[s[i]] >= start:
                start = char_dict[s[i]]+1
            max_len = max(max_len, i-start+1)
            char_dict[s[i]] = i
        return max_len 


