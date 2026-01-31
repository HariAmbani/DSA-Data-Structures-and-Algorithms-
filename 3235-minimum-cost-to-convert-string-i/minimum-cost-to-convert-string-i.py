class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        # actually it is graph problem
        # implementing flowd warshal to find the minimum distance between 2 letters

        #predesecors matrix
        #pre_mat = [([-1] * 26) for _ in range(26)]

        #distancc matrix
        dis_mat = [([float("inf")] * 26) for _ in range(26)]

        for i in range(len(original)):
            #if original[i] != changed[i]
            dis_mat[ord(original[i])-97][ord(changed[i])-97] = min(dis_mat[ord(original[i])-97][ord(changed[i])-97], cost[i])
            #pre_mat[ord(original[i])-97][ord(changed[i])-97] = original[i]
        
        for i in range(26):
            dis_mat[i][i] = 0
        

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dis_mat[i][j] = min(dis_mat[i][j], dis_mat[i][k]+dis_mat[k][j])
        
        ans = 0
        for i in range(len(source)):
            if source[i] == target[i]:
                continue
            elif dis_mat[ord(source[i])-97][ord(target[i])-97] == float("inf"):
                return -1
            else:
                ans += dis_mat[ord(source[i])-97][ord(target[i])-97]

        return ans
    