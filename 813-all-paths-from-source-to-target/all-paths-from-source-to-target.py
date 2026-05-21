class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        
        ans = []

        def dfs(path, cur):
            if cur == len(graph)-1:
                ans.append(path+[cur])
            else:
                for j in graph[cur]:
                    dfs(path+[cur], j)

        for i in graph[0]:
            dfs([0], i)
        
        return ans