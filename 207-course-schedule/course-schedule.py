class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites:
            return True
        
        to_see = []

        for i in range(numCourses):
            to_see.append(i)
        
        path_map_to = {}
        path_map_from = {}

        for i,j in prerequisites:
            
            if i in path_map_to:
                if j in path_map_to[i]:
                    return False
            
            if i in path_map_from:
                path_map_from[i] += 1
            else:
                path_map_from[i] = 1
            
            if j in path_map_to:
                path_map_to[j].append(i)
            else:
                path_map_to[j] = [i]
        
        print(path_map_from)
        print(path_map_to)
        #print(to_see)
        
        stack = []
        seen = 0

        for i in to_see:
            if i not in path_map_from:
                stack.append(i)
                seen += 1
        
        while stack:
            cur = []
            for i in stack:
                print("i : ",i)
                for j in path_map_to.get(i, []):
                    print("j : ",j)
                    if path_map_from[j] == 1:
                        cur.append(j)
                        seen += 1
                        del path_map_from[j]
                    else:
                        path_map_from[j] -= 1
                stack = cur
                print("stack : ", stack)
                
        if seen == numCourses:
            return True
        else:
            return False
        


            
            



        