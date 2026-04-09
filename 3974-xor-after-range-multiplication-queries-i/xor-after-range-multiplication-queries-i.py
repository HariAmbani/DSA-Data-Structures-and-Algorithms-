class Solution(object):
    def xorAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        lq = len(queries)
        ln = len(nums)
        MOD = (10**9)+7
        for i in range(lq):
            l, r, k, v = queries[i]
            idx = l
            max_ind = min(r, ln-1)
            while idx <= max_ind:
                nums[idx] = (nums[idx]*v) % MOD
                idx += k

        ans = nums[0]
        for i in range(1, ln):
            ans ^= nums[i]
        
        return ans
        
        