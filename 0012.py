class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        str = ""
        while num > 0:
            if num >= 1000:
                str += "M"
                num -= 1000
            elif num >= 900 and num < 1000:
                str += "CM"
                num -= 900
            elif num >= 500 and num < 900:
                str += "D"
                num -= 500
            elif num >= 400 and num < 500:
                str += "CD"
                num -= 400
            elif num >= 100 and num < 400:
                str += "C"
                num -= 100
            elif num >= 90 and num < 100:
                str += "XC"
                num -= 90
            elif num >= 50 and num < 90:
                str += "L"
                num -= 50
            elif num >= 40 and num < 50:
                str += "XL"
                num -= 40
            elif num >= 10 and num < 40:
                str += "X"
                num -= 10
            elif num >= 9 and num < 10:
                str += "IX"
                num -= 9
            elif num >= 5 and num < 9:
                str += "V"
                num -= 5
            elif num >= 4 and num < 5:
                str += "IV"
                num -= 4
            else:
                str += "I"
                num -= 1
        return str