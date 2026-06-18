from collections import defaultdict
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) == 1:
            return False 
            
        sum_dict = defaultdict(int)
        sum_dict[0] = 0

        cur_sum = 0
        zero_count = []

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count.append(i)
                continue
            cur_sum = (cur_sum + nums[i])%k
            if cur_sum in sum_dict and (i-sum_dict[cur_sum]) >= 1 and (nums[i] % k != 0 or ((nums[i]+nums[i-1]) % k == 0)) :
                return True
            if cur_sum not in sum_dict:
                sum_dict[cur_sum] = i
        
        for i in zero_count:
            if i == 0:
                if nums[i+1]%k == 0:
                    return True
            elif i == len(nums)-1:
                if nums[i-1]%k == 0:
                    return True
            else:
                if nums[i-1]%k == 0 or nums[i+1]%k == 0:
                    return True
        
        return False

        

        