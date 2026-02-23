class Solution(object):
    def rob(self, nums):

        def helper(arr):
            rob1, rob2 = 0, 0
            for n in arr:
                temp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        return max(nums[0], helper(nums[:-1]), helper(nums[1:]))