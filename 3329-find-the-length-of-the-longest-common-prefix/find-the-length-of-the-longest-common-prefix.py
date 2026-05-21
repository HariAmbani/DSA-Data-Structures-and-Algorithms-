class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        prefixes = set()
        
        for i in arr1:
            s = str(i)
            l = len(s)
            for j in range(l):
                if s[:j+1] not in prefixes:
                    prefixes.add(s[:j+1])

        maxi = 0

        for j in arr2:
            s = str(j)
            l = len(s)
            for j in range(l):
                if s[:j+1] in prefixes:
                    print(s[:j+1])
                    maxi = max(maxi, j+1)
        
        return maxi
        