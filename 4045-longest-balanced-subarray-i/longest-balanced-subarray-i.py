class Solution(object):
    def longestBalanced(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0
        i = 0

        while i < n and ans < n-i:
            odds = set()
            evens = set()
            for j in range(i, n):
                if nums[j] % 2 == 0:
                    evens.add(nums[j])
                elif nums[j] % 2 == 1:
                    odds.add(nums[j])
                if len(odds)-len(evens) == 0 and len(odds) != 0:
                    ans = max(ans, j-i+1)
            i += 1
        
        return ans