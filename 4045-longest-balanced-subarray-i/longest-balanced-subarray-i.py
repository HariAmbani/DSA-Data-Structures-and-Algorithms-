class Solution(object):
    def longestBalanced(self, nums):
        n = len(nums)
        ans = 0

        for i in range(n):
            odds, evens = set(), set()

            for j in range(i, n):
                if nums[j] % 2 == 0:
                    evens.add(nums[j])
                else:
                    odds.add(nums[j])

                if len(odds) == len(evens) and len(odds) > 0:
                    ans = max(ans, j - i + 1)

        return ans
