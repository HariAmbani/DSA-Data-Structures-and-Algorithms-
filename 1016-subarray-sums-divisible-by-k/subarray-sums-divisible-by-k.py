from collections import defaultdict
class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cur_sum = 0
        ans = 0

        rem_dict = defaultdict(int)
        rem_dict[0] = 1

        for i in nums:
            cur_sum = (cur_sum+i)%k
            ans += rem_dict[cur_sum]
            rem_dict[cur_sum] += 1

        return ans 

        