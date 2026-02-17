from collections import deque

class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        prev_row = [poured] #initial

        for row in range(1, query_row+1):
            cur_row = [0.0]*(row+1)
            for i in range(row):
                extra = prev_row[i]-1
                if extra > 0.0:
                    cur_row[i] += extra * 0.5
                    cur_row[i+1] += extra * 0.5
            prev_row = cur_row
        return min(1, prev_row[query_glass])