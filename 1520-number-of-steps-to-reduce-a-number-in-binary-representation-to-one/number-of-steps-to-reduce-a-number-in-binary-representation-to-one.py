class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        i = len(s) - 1
        slist = list(s)

        while i != 0:
            ans += 1
            if slist[i] == "1":
                j = i-1
                while j >= 0 and slist[j] == "1":
                    slist[j] = "0"
                    j -= 1
                if j < 0:
                    slist[0] = "1"
                    slist[i] = "0"
                    i += 1
                    if i > len(s)-1:
                        slist.append("0")
                    else:
                        slist[i] = "0"
                else:
                    slist[j] = "1"
                    slist[i] = "0"
            else:
                i -= 1  
        
        return ans


        