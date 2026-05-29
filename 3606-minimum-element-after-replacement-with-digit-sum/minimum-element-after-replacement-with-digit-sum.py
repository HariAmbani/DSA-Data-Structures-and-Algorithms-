class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mini = float('inf')
        for i in nums:
            cur = 0
            while i > 0:
                cur += i%10
                i = int(i/10)
            mini = min(mini, cur)
        
        return mini


        