class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []

        for i in s:
            if len(res) > 0:
                if i == '*':
                    del res[-1]
                elif i == '#':
                    res += res
                elif i == '%':
                    res = res[::-1]
                else:
                    res.append(i)
            elif i not in ['*', '#', '%']:
                res.append(i)

        return "".join(res)

        