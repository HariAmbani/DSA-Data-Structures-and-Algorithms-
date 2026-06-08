class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        n = len(nums)
        new = [0]*n
        
        less = 0
        more = 0
        same = 0

        for i in nums:
            if i < pivot:
                less += 1
            elif i > pivot:
                more += 1
            else:
                same += 1
        
        less_pos = 0
        same_pos = less
        more_pos = less + same

        for i in nums:
            if i < pivot:
                new[less_pos] = i
                less_pos += 1
            elif i > pivot:
                new[more_pos] = i
                more_pos += 1
            else:
                new[same_pos] = i
                same_pos += 1
    
        nums = new
        return nums
                