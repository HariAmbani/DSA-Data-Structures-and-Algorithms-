class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(intervals)

        if n == 1:
            return intervals

        intervals.sort(key=lambda x:x[0])
        
        ans = []

        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1, n):
            if intervals[i][0] <= end:
                end = max(end, intervals[i][1])
            
            else:
                ans.append([start, end])
                start, end = intervals[i]
            
        ans.append([start, end])

        
        return ans

