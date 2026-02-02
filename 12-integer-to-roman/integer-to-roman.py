class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        int_to_roman = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }

        ans = ""
        while num > 0:
            if num >= 1000:
                cur = num//1000
                ans += int_to_roman[1000]*cur
                num %= 1000
            if num >= 900:
                num -= 900
                ans += int_to_roman[900]
            if num >= 500:
                num -= 500
                ans += int_to_roman[500]
            if num >= 400:
                num -= 400
                ans += int_to_roman[400]
            if num >= 100:
                cur = num//100
                ans += int_to_roman[100]*cur
                num %= 100
            if num >= 90:
                num -= 90
                ans += int_to_roman[90]
            if num >= 50:
                num -= 50
                ans += int_to_roman[50]
            if num >= 40:
                num -= 40
                ans += int_to_roman[40]
            if num >= 10:
                cur = num//10
                ans += int_to_roman[10]*cur
                num %= 10
            if num >= 9:
                num -= 9
                ans += int_to_roman[9]
            if num >= 5:
                num -= 5
                ans += int_to_roman[5]
            if num >= 4:
                num -= 4
                ans += int_to_roman[4]
            if num >= 1:
                cur = num//1
                ans += int_to_roman[1]*cur
                num -= cur
        
        return ans


                
                





        

        