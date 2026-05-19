class Solution(object):
    def twoSum(self, nums, target):
        val_dict = {}
        for ind, val in enumerate(nums):
            want = target - nums[ind]
            if want in val_dict:
                return [ind, val_dict[want]]
            val_dict[nums[ind]] = ind

        