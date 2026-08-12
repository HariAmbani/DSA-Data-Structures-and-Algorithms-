class Solution(object):
    def maxSubarrayLength(self, nums, k):
        count = {}
        left = 0
        ans = 0

        for right in range(len(nums)):
            if nums[right] in count:
                count[nums[right]] += 1
                if count[nums[right]] > k:
                    while count[nums[right]] > k:
                        count[nums[left]] -= 1
                        left += 1
            else:
                count[nums[right]] = 1
            ans = max(ans, right-left+1)
        
        return ans