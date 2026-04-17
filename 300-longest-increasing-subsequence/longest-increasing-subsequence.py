class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n == 1:
            return 1

        lis = [1]*n

        maxi = 0

        for i in range(len(nums)-2, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], 1+lis[j])
            maxi = max(maxi, lis[i])
        
        return maxi
        
        
            

        