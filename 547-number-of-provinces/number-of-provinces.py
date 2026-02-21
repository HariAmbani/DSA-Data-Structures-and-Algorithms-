class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)

        to_see = set()
        ans = 0

        for i in range(n):
            to_see.add(i)

        graph = {i:set() for i in range(n)}

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    graph[i].add(j)

        print(graph)

        visited = set()

        def dfs(node):
            visited.add(node)
            for i in graph[node]:
                if i not in visited:
                    print("-- ",i)
                    dfs(i)

        for i in range(n):
            if i not in visited:
                print(i)
                ans += 1
                dfs(i)
        
        return ans




        