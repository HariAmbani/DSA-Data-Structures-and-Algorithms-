class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        ans = 0

        rows = len(mat)
        cols = len(mat[0])

        indexes_not_to_check = set()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1 and (i,j) not in indexes_not_to_check:
                    a_found = 0
                    b_found = 0
                    for a in range(rows):
                        if a == i:
                            continue
                        if mat[a][j] == 1:
                            a_found = 1
                            indexes_not_to_check.add((a,j))
                            break
                    if a_found == 0:
                        for b in range(cols):
                            if b == j:
                                continue
                            if mat[i][b] == 1:
                                b_found = 1
                                indexes_not_to_check.add((i,b))
                                break
                        if b_found == 0:
                            ans += 1
        
        return ans

        