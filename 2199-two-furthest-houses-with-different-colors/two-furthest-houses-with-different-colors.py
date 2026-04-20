class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        n = len(colors)
        ans = 0

        i = 0
        j = n

        while i < j:
            end = j
            while end-i > ans:
                if colors[i] != colors[end-1]:
                    ans = max(ans, abs(i-end)-1)
                end -= 1
            i += 1
            j = n
        
        return ans


        