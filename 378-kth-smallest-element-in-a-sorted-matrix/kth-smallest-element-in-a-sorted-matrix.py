import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        side = len(matrix)

        if side == 1:
            return matrix[0][0]

        sorted_elements = matrix[0]

        for i in range(1, side):
            for j in range(side):
                heapq.heappush(sorted_elements, matrix[i][j])

        for i in range(k):
            ans = heapq.heappop(sorted_elements)
        
        return ans


        