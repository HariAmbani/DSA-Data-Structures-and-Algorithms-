class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        remainders = {0: -1}
        prefix_sum = 0
    
        for i, num in enumerate(nums):
            prefix_sum += num
            remainder = prefix_sum % k
            if remainder in remainders:
                if i - remainders[remainder] > 1:
                    return True
            else:
                remainders[remainder] = i
        return False        