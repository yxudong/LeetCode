class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_1 = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        dict_2 = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

        l = len(s)
        if l == 1:
            return dict_1[s[0]]

        i, sum = 0, 0
        while i < l - 1:
            if s[i:i+2] in dict_2.keys():
                sum += dict_2[s[i:i+2]]
                i += 2
            else:
                sum += dict_1[s[i]]
                i += 1
        if i == l - 1:
            sum += dict_1[s[i]]

        return sum