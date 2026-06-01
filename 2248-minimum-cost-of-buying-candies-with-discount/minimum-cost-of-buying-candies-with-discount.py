class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.sort()
        ans = 0

        i = len(cost)-1
        while i >= 0:
            if i-1 >= 0:
                ans += cost[i] + cost[i-1]
            else:
                ans += cost[i]
            i -= 3
        
        return ans