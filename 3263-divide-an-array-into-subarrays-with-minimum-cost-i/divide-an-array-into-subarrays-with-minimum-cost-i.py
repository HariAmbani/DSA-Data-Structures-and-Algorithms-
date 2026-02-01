class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = nums[0]
        second = float("inf")
        third = float("inf")
        for i in nums[1:]:
            if i < second:
                third = second
                second = i
            elif i < third:
                third = i
        
        return (first+second+third)
        