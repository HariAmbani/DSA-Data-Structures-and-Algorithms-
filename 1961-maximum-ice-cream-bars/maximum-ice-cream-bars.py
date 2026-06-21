class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()

        count = 0

        i = 0
        while coins > 0 and i < len(costs):
            if coins >= costs[i]:
                count += 1
            coins -= costs[i]
            i += 1
        
        return count
        