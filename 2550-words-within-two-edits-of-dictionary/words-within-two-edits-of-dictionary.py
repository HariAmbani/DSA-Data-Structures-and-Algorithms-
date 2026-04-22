class Solution(object):
    def twoEditWords(self, queries, dictionary):
        """
        :type queries: List[str]
        :type dictionary: List[str]
        :rtype: List[str]
        """
        ans = []

        word_set = set()

        def differ(w1, w2):
            count = 0
            i = 0
            while i < len(w1) and count <= 2:
                if w1[i] != w2[i]:
                    count += 1
                i += 1
            if count > 2:
                return False
            else:
                return True

        for i in dictionary:
            word_set.add(i)
        
        for i in queries:
            if i in word_set:
                ans.append(i)
            else:
                for j in dictionary:
                    if differ(i, j):
                        ans.append(i)
                        break
        
        return ans
            
        