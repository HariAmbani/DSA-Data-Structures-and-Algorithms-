class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        if amount == 0:
            return 0

        coins_needed = [amount+1] * (amount+1)
        coins_needed[0] = 0

        for amo in range(1, amount+1):
            for coin in coins:
                if amo - coin >= 0:
                    coins_needed[amo] = min(coins_needed[amo], 1 + coins_needed[amo-coin])

        return coins_needed[amo] if coins_needed[amo] < amount+1 else -1 

                



        