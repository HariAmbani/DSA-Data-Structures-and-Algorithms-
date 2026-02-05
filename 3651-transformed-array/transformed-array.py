class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0]*n

        for i in range(n):
            if nums[i] == 0:
                result[i] = nums[i]
            if nums[i] > 0:
                j = i
                j = (j+nums[i])%n
                result[i] = nums[j]
            else:
                j = i
                j = (j-abs(nums[i]))%n
                result[i] = nums[j]
        
        return result

        
        