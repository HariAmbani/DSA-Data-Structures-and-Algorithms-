class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        mini = float("inf")
        for i in range(len(nums)):
            if nums[i] == target:
                mini = min(mini, abs(i-start))
        
        return mini
        