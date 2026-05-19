class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        if ((nums1[0] > nums2[-1]) or (nums1[-1] < nums2[0])):
            return -1

        for i in nums1:
            for j in nums2:
                if i == j:
                    return i
                elif i < j:
                    break
        
        return -1
                    
        