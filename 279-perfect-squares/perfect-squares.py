class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        coins = []

        i = 1
        while (i*i) <=  n:
            coins.append(i*i)
            i += 1
        
        if coins[-1] == n:
            return 1

        #dp
        coins_needed = [n+1] * (n+1)
        coins_needed[0] = 0

        for amo in range(1, n+1):
            for coin in coins:
                if amo - coin >= 0:
                    coins_needed[amo] = min(coins_needed[amo], 1 + coins_needed[amo-coin])

        return coins_needed[amo] if coins_needed[amo] < n+1 else -1 


        