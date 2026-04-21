from collections import defaultdict, deque, Counter

class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        n = len(source)
        
        # Step 1: Build graph
        graph = defaultdict(list)
        for i, j in allowedSwaps:
            graph[i].append(j)
            graph[j].append(i)
        
        visited = set()
        ans = 0
        
        # Step 2: Traverse each connected component
        for i in range(n):
            if i not in visited:
                queue = deque([i])
                component = []
                
                while queue:
                    node = queue.popleft()
                    
                    if node in visited:
                        continue
                    
                    visited.add(node)
                    component.append(node)
                    
                    for nei in graph[node]:
                        if nei not in visited:
                            queue.append(nei)
                
                # Step 3: Count values in this component
                count = Counter()
                for idx in component:
                    count[source[idx]] += 1
                
                # Step 4: Try matching target
                for idx in component:
                    if count[target[idx]] > 0:
                        count[target[idx]] -= 1
                    else:
                        ans += 1
        
        return ans