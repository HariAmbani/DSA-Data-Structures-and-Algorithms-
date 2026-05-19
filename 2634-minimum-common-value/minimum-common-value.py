class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        ans = -1

        for i in nums1:
            for j in nums2:
                if i == j:
                    return i
                elif i < j:
                    break
        
        return -1
                    
        