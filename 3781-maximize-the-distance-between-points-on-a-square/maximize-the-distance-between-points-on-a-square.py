import bisect

class Solution(object):
    def maxDistance(self, side, points, k):
        perimeter = 4 * side

        # map to 1D
        arr = []
        for x, y in points:
            if y == 0:
                arr.append(x)
            elif x == side:
                arr.append(side + y)
            elif y == side:
                arr.append(3 * side - x)
            else:
                arr.append(4 * side - y)

        arr.sort()
        n = len(arr)

        extended = arr + [x + perimeter for x in arr]

        # check function
        def can(d):
            for i in range(n):
                count = 1
                cur = extended[i]

                for _ in range(k - 1):
                    nxt = bisect.bisect_left(extended, cur + d)
                    if nxt >= i + n:
                        break
                    cur = extended[nxt]
                    count += 1

                if count == k:
                    # circular check
                    if cur - extended[i] <= perimeter - d:
                        return True
            return False

        # binary search
        low, high = 0, perimeter
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            if can(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans