class Solution(object):
    def canReach(self, s, minJump, maxJump):
        n = len(s)

        dp = [False] * n
        dp[0] = True

        reachable = 0

        for i in range(1, n):

            # add new index entering window
            if i - minJump >= 0 and dp[i - minJump]:
                reachable += 1

            # remove old index leaving window
            if i - maxJump - 1 >= 0 and dp[i - maxJump - 1]:
                reachable -= 1

            if s[i] == '0' and reachable > 0:
                dp[i] = True

        return dp[-1]