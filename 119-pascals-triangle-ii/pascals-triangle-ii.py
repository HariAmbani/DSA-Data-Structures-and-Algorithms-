class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        pascal_triangle = [1,1] 
        
        for i in range(2, rowIndex+1):
            s = [1]
            for j in range(1, len(pascal_triangle)):
                s.append(pascal_triangle[j-1]+pascal_triangle[j])
            s.append(1)
            pascal_triangle = s
        return pascal_triangle
        