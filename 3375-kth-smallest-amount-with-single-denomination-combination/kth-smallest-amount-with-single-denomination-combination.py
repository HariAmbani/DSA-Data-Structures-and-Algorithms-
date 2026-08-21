class Solution(object):
    def findKthSmallest(self, coins, k):
        """
        :type coins: List[int]
        :type k: int
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b

            return a

        n = len(coins)

        # Precompute LCM for every subset
        subsets = []

        for mask in range(1, 1 << n):
            lcm = 1
            bits = 0

            for i in range(n):
                if mask & (1 << i):
                    bits += 1

                    lcm = lcm // gcd(lcm, coins[i]) * coins[i]

            subsets.append((lcm, bits))

        def count(x):
            total = 0

            for lcm, bits in subsets:

                if lcm > x:
                    continue

                multiples = x // lcm

                if bits % 2 == 1:
                    total += multiples
                else:
                    total -= multiples

            return total

        # The answer cannot be greater than k * minimum coin.
        left = 1
        right = min(coins) * k

        while left < right:
            mid = left + (right - left) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left

        