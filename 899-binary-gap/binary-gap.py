class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """

        def decimal_to_binary_converter(n):
            ans = ""
            while n > 0:
                if n % 2 == 0:
                    ans += "0"
                else:
                    ans += "1"
                n //= 2
            return ans
        
        binary = decimal_to_binary_converter(n)
        print(binary)
        
        ans = 0
        i = 0
        
        while i < len(binary):
            if binary[i] == "1":
                print("start")
                count = 1
                i += 1
                print(i)
                while i < len(binary) and binary[i] != "1":
                    print("i : ", i)
                    print("count : ", count)
                    count += 1
                    i += 1
                if i < len(binary):
                    ans = max(ans, count)
            else:
                i += 1
         
        return ans 
        