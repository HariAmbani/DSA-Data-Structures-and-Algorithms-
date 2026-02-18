import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        n = len(matrix)

        sort_array = []

        for i in range(n):
            sort_array.append([matrix[i][0], i, 0])
        
        for i in range(k):
            ans,r,c = heapq.heappop(sort_array)

            if c+1 < n:
                heapq.heappush(sort_array, [matrix[r][c+1],r,c+1])
        return ans 
