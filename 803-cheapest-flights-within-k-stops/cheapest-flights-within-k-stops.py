class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """

        INF = float('inf')
        cost_to_reach = [INF]*n
        cost_to_reach[src] = 0

        for _ in range(k+1):
            temp = cost_to_reach[:]
            for i in flights:
                source, destination, cost = i
                if temp[source] != INF:
                    temp[destination] = min(temp[destination], cost_to_reach[source]+cost)
            cost_to_reach = temp
        
        return cost_to_reach[dst] if cost_to_reach[dst] != INF else -1