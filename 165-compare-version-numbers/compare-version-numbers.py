class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split(".")
        v2 = version2.split(".")

        i = 0
        a = len(v1)
        b = len(v2)

        if a>b:
            greater = "v1"
            n = b
            m = a
        else:
            greater = "v2"
            n = a
            m = b
        


        for i in range(n):
            if int(v1[i]) > int(v2[i]):
                print("1")
                return 1
            elif int(v1[i]) < int(v2[i]):
                print("2")
                return -1
        
        if greater == "v1":
            for j in range(n, m):
                if int(v1[j]) != 0:
                    print("3")
                    return 1
        else:
            for j in range(n, m):
                if int(v2[j]) != 0:
                    print("4")
                    return -1

        return 0
        