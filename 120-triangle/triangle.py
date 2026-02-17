class Solution(object):
    def minimumTotal(self, triangle):
        dp = [0]*(len(triangle)+1)

        for rows in triangle[::-1]:
            for i, v in enumerate(rows): 
                dp[i] = v + min(dp[i], dp[i+1])

        return dp[0] 
        
                
