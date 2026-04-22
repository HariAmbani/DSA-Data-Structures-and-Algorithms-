from collections import defaultdict, deque, Counter

class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        n = len(source)
        ans = 0        

        if len(allowedSwaps) == 0:
            for i in range(n):
                if source[i] != target[i]:
                    ans += 1
            
            return ans


        graph = defaultdict(list)
        for i, j in allowedSwaps:
            graph[i].append(j)
            graph[j].append(i)
        
        to_visit = []
        visited = set()
        connected = []
        
        for key in graph.keys():
            if key not in visited:
                cur = []
                q = deque([key])
                while q:
                    now = q.popleft()
                    if now not in visited:
                        cur.append(now)
                        visited.add(now)
                    for val in graph[now]:
                        if val not in visited:
                            q.append(val)
                connected.append(cur)

        print(connected)

        for values in connected:
            count = Counter()

            for val in values:
                count[source[val]] += 1

            for val in values:
                if count[target[val]] > 0:
                    count[target[val]] -= 1
                else:
                    ans += 1


        for i in range(n):
            if i not in visited and source[i] != target[i]:
                ans += 1
        
        return ans
            


        
        
                
        return ans