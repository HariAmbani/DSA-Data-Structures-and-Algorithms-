class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        ans = 0

        rows = len(mat)
        cols = len(mat[0])

        rows_contain_one = set()
        cols_contain_one = set()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
                    a_found = 0
                    b_found = 0
                    for a in range(rows):
                        if a == i:
                            continue
                        if mat[a][j] == 1:
                            a_found = 1
                            break
                    if a_found == 0:
                        for b in range(cols):
                            if b == j:
                                continue
                            if mat[i][b] == 1:
                                b_found = 1
                                break
                        if b_found == 0:
                            ans += 1
        
        return ans

        