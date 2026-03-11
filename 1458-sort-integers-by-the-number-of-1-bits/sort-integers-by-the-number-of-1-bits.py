import heapq
class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        binaries = []
        binaries_count = []

        for i in arr:
            bi = bin(i)
            binaries.append([bi[2:], i])
        
        for i in binaries:
            coun = 0
            for j in i[0]:
                if j == "1":
                    coun += 1
            
            heapq.heappush(binaries_count, (coun, i[1]))
        
        ans = []

        for i in range(len(arr)):
            cur = heapq.heappop(binaries_count)
            ans.append(cur[1])
        
        return ans
                
                

        

        