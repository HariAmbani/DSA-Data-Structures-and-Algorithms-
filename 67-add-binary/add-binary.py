class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        lena = len(a)
        lenb = len(b)

        if lena > lenb:
            a,b = b,a
            lena, lenb = lenb, lena

        ans = ""
        carry = 0
        
        for i in range(lena):
            if carry == 0:
                if a[lena-1-i] == "1" and b[lenb-1-i] == "1":
                    ans = "0"+ans
                    carry = 1
                elif a[lena-1-i] == "1" or b[lenb-1-i] == "1":
                    ans = "1"+ans
                else:
                    ans = "0"+ans
            else:
                if a[lena-1-i] == "1" and b[lenb-1-i] == "1":
                    ans = "1"+ans
                elif a[lena-1-i] == "1" or b[lenb-1-i] == "1":
                    ans = "0"+ans
                else:
                    ans = "1"+ans
                    carry = 0
        
        if carry == 0:
            ans = b[:lenb-lena]+ans
            return ans
        else:
            for i in range(lena, lenb):
                if b[lenb-i-1] == "1":
                    ans = "0"+ans
                else:
                    ans = "1"+ans
                    ans = b[:lenb-i-1]+ans
                    return ans

        if carry == 1:
            ans = "1"+ans
        return ans

            

        