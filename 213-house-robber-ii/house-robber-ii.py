class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]

        nums_1 = nums[:len(nums)-1]
        
        rob1, rob2 = 0, 0

        for i in nums_1:
            temp = max(rob1+i, rob2)
            rob1 = rob2
            rob2 = temp
        
        rob3, rob4 = 0, 0

        nums_2 = nums[1:]

        for i in nums_2:
            temp = max(rob3+i, rob4)
            rob3 = rob4
            rob4 = temp
        
        return max(rob2, rob4)
        