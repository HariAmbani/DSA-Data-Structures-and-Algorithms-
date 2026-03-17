class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        empty = [0] * (amount-1)
        empty.append(1)

        coins.sort()
        coin_len = len(coins)
        
        dp = [[0]*(amount) + [1] for _ in range(coin_len)]

        for i in range(amount-1, -1, -1):
            if amount-i-coins[-1] >= 0:
                dp[coin_len-1][i] = dp[coin_len-1][i+coins[-1]]
            else:
                dp[coin_len-1][i] = 0
        
        for i in range(coin_len-2, -1, -1):
            for j in range(amount-1, -1, -1):
                if amount-j-coins[i] >= 0:
                    dp[i][j] = dp[i][j+coins[i]] + dp[i+1][j]
                else:
                    dp[i][j] = 0
        
        return dp[0][0]
        


        


        