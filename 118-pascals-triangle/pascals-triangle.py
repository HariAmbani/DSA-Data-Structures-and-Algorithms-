class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]
        l = [[1], [1,1]]
        for i in range(2, numRows):
            s = [1]
            for j in range(1, len(l[-1])):
                s.append(l[i-1][j-1]+l[i-1][j])
            s.append(1)
            l.append(s)
        return l

        