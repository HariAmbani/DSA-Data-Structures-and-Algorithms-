class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        ans = "0"

        for i in n:
            if i > ans:
                ans = i
        
        return int(ans)

        