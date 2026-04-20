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
            start = i
            end = j
            while end-start > ans:
                if colors[start] != colors[end-1]:
                    ans = max(ans, abs(start-end)-1)
                end -= 1
            i += 1
            j = n
        
        return ans


        