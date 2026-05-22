class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        g_max = c_max = nums[0]

        for i in range(1, len(nums)):
            c_max = max(c_max+nums[i], nums[i])
            g_max = max(g_max, c_max)
        return g_max