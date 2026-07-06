class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x:(x[0], -x[1]))
        n = len(intervals)

        ans = n

        i = 0

        while i < n-1:
            if intervals[i+1][1] <= intervals[i][1]:
                changed = 1
                ans -= 1
                if i+2 < n:
                    j = i+2
                    while ((j < n) and (intervals[j][1] <= intervals[i][1])):
                        j += 1
                        ans -= 1
                    i = j
                else:
                    break
            else:
                i += 1
        
        return ans






