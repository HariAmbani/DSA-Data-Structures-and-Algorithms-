class Solution(object):
    def largestSubmatrix(self, matrix):
        rows, cols = len(matrix), len(matrix[0])

        # Step 1: build heights
        for i in range(1, rows):
            for j in range(cols):
                if matrix[i][j]:
                    matrix[i][j] += matrix[i-1][j]

        ans = 0

        for i in range(rows):
            row = sorted(matrix[i], reverse=True)
            for j in range(cols):
                ans = max(ans, row[j] * (j + 1))

        return ans