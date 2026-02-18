import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        n = len(matrix)

        # Min heap will store: (value, row, col)
        heap = []

        # Step 1: Push first element of each row
        for r in range(n):
            heapq.heappush(heap, (matrix[r][0], r, 0))

        # Step 2: Pop k times
        for _ in range(k):
            val, r, c = heapq.heappop(heap)

            # Step 3: Push next element in same row
            if c + 1 < n:
                heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))

        return val
