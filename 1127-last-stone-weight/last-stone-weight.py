import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)

        if n == 1:
            return stones[0]

        max_heap = []
        
        for i in stones:
            heapq.heappush(max_heap, -i)
        
        for i in range(n-1):
            a = heapq.heappop(max_heap)
            b = heapq.heappop(max_heap)
            heapq.heappush(max_heap, a-b)
        
        return -(max_heap[0])
        
        

        