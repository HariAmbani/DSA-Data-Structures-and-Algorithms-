import heapq
class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        for i in range(len(tasks)):
            tasks[i].append(i)
        
        tasks.sort(key=lambda x:(x[0], x[1]))

        process = [tasks[0][2]]
        time = tasks[0][0]+tasks[0][1]
        heap = []
        j = 1

        while j < len(tasks):
            while j < len(tasks) and time >= tasks[j][0]:
                heapq.heappush(heap, [tasks[j][1], tasks[j][2]])
                j += 1
            if heap:
                ptime, index = heapq.heappop(heap)
                time += ptime
                process.append(index)
            else:
                time = tasks[j][0]
        
        while heap:
            ptime, index = heapq.heappop(heap)
            time += ptime
            process.append(index)

        return process



        


        