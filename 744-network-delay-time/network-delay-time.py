import heapq
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 1:
            return 0
        
        adj_list = {}

        for i in range(1,n+1):
            adj_list[i] = []
        
        for src, dst, wt in times:
            adj_list[src].append([dst, wt])
        
        shortest = {}
        minheap = [[0, k]]
        time = 0

        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in shortest:
                continue
            shortest[n1] = w1
            if len(shortest) == n:
                time += w1
            for n2, w2 in adj_list[n1]:
                if n2 not in shortest:
                    heapq.heappush(minheap, [w1+w2, n2])
        
        if len(shortest) == n:
            return time
        else:
            return -1

        





        