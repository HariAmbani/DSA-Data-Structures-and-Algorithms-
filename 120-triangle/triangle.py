class Solution(object):
    def minimumTotal(self, triangle):
        if len(triangle) == 1:
            return triangle[0][0]

        for i in range(len(triangle)):
            triangle[len(triangle)-1][i] = [triangle[len(triangle)-1][i],0]

        for i in range(len(triangle)-2, -1, -1):
            for j in range(i+1):
                triangle[i][j] = [triangle[i][j], min((triangle[i+1][j][0]+triangle[i+1][j][1]), (triangle[i+1][j+1][0]+triangle[i+1][j+1][1]))]

        res = 0
        for i in triangle[0]:
            for j in i:
                res += j
        
        return res
                
