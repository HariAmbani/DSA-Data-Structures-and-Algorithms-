class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        i = 0
        count1 = 0
        count2 = 0
        count3 = 0

        while i < len(nums)-1 and nums[i] < nums[i+1]:
            count1 += 1
            i += 1
        if i<len(nums)-1 and nums[i] == nums[i+1]:
            return False
        while i < len(nums)-1 and nums[i] > nums[i+1]:
            count2 += 1
            i += 1
        if i<len(nums)-1 and nums[i] == nums[i+1]:
            return False
        while i < len(nums)-1 and nums[i] < nums[i+1]:
            count3 += 1
            i += 1
        
        if i != len(nums)-1:
            return False
        else:
            if count1==0 or count2==0 or count3==0:
                return False
            else:
                return True
            
        