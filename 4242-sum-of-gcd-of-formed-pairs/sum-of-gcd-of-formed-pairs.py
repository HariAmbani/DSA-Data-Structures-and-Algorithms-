class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a,b):
            if a%b == 0:
                return b
            return gcd(b, a%b)

        ans = 0
        prefixGCD = []
        cur_max = nums[0]

        for i in nums:
            cur_max = max(cur_max, i)
            prefixGCD.append(gcd(i, cur_max))
        
        prefixGCD.sort()
        n = len(prefixGCD)

        for i in range(len(nums)//2):
            ans += gcd(prefixGCD[n-1-i], prefixGCD[i])
        
        return ans

