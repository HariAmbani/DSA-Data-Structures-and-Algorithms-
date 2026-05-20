from collections import defaultdict
class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        dict_one = defaultdict(int)
        dict_two = defaultdict(int)

        n = len(A)

        c = []

        for i in range(n):
            if A[i] == B[i]:
                if i == 0:
                    c.append(1)
                else:
                    c.append(c[-1]+1)
            else:
                if i == 0:
                    cur = 0
                else:
                    cur = c[-1]
                if A[i] in dict_two:
                    cur += 1
                    if dict_two[A[i]] == 1:
                        del dict_two[A[i]]
                    else:
                        dict_two[A[i]] -= 1
                else:
                    dict_one[A[i]] += 1

                if B[i] in dict_one:
                    cur += 1
                    if dict_one[B[i]] == 1:
                        del dict_one[B[i]]
                    else:
                        dict_one[B[i]] -= 1
                else:
                    dict_two[B[i]] += 1 
                c.append(cur)
        
        return c
