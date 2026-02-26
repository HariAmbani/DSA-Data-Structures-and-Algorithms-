from collections import defaultdict
class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        def helper(w):
            dic = {}
            for i in w:
                if i in dic:
                    dic[i] += 1
                else:
                    dic[i] = 1
            return dic
        
        ans = 0
        
        i = 1
        a = s[:i]
        b = s[i:]
        w1 = helper(a)
        w2 = helper(b)

        if len(w1) == len(w2):
            ans += 1

        for i in range(0, len(b)-1):
            cur = b[i]
            if cur in w1:
                w1[cur] += 1
            else:
                w1[cur] = 1
            if w2[cur] == 1:
                del w2[cur]
            else:
                w2[cur] -= 1
            if len(w1) == len(w2):
                ans += 1

        return ans
        

        