class Solution(object):
    def minMirrorPairDistance(self, nums):
        last_seen = {}   # reversed value -> index
        mini = float('inf')

        for i, num in enumerate(nums):
            if num in last_seen:
                mini = min(mini, i - last_seen[num])

            rev = int(str(num)[::-1])
            last_seen[rev] = i

        return mini if mini != float('inf') else -1