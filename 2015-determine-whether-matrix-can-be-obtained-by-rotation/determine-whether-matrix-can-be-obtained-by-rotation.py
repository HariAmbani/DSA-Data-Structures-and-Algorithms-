class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        if mat == target:
            return True

        size = len(mat)

        ninety = list(zip(*mat))

        can = True
        for i in range(size):
            if target[i] != list(ninety[i])[::-1]:
                can = False
                break

        if can == True:
            return True
        
        can = True
        for i in range(size):
            if target[i] != mat[size-i-1][::-1]:
                can = False
                break

        if can == True:
            return True
        
        can = True
        for i in range(size):
            if target[i] != list(ninety[size-i-1]):
                can = False
                break
        
        if can == True:
            return True
        
        return False


        

        