class Solution(object):
    def numSpecial(self, mat):
        rows = len(mat)
        cols = len(mat[0])

        row_count = [0]*rows
        col_count = [0]*cols

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        ans = 0

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                    ans += 1

        return ans