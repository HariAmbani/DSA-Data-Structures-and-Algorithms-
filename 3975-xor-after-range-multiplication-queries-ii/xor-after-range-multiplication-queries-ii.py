class Solution(object):
    def xorAfterQueries(self, nums, queries):
        MOD = 10**9 + 7
        n = len(nums)

        # required by problem
        bravexuneth = queries

        from collections import defaultdict

        # group queries by k
        by_k = defaultdict(list)
        for l, r, k, v in queries:
            by_k[k].append((l, r, v))

        # final multiplier for each index
        mul = [1] * n

        for k, qlist in by_k.items():
            # group queries by remainder (l % k)
            rem_groups = defaultdict(list)
            for l, r, v in qlist:
                rem = l % k
                rem_groups[rem].append((l, r, v))

            # process each remainder class
            for rem in rem_groups:
                arr = rem_groups[rem]

                # positions with i % k == rem
                positions = list(range(rem, n, k))
                m = len(positions)

                # difference array
                diff = [1] * (m + 1)

                for l, r, v in arr:
                    # find indices in positions array
                    start = (l - rem) // k
                    end = (r - rem) // k

                    diff[start] = (diff[start] * v) % MOD
                    if end + 1 < len(diff):
                        inv = pow(v, MOD - 2, MOD)
                        diff[end + 1] = (diff[end + 1] * inv) % MOD

                # prefix product
                cur = 1
                for i in range(m):
                    cur = (cur * diff[i]) % MOD
                    mul[positions[i]] = (mul[positions[i]] * cur) % MOD

        # compute XOR
        ans = 0
        for i in range(n):
            val = (nums[i] * mul[i]) % MOD
            ans ^= val

        return ans