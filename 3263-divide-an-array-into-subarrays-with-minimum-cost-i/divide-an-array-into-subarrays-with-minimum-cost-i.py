class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = nums[0]
        nums_two = nums[1:]
        nums_two.sort()
        return first+nums_two[0]+nums_two[1]
        