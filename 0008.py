class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str_ = str.lstrip()
        if not str_:
            return 0
        
        if str_[0] == "-" or str_[0] == "+":
            new_str = str_[0]
            for i in range(1, len(str_)):
                if str_[i].isdigit():
                    new_str += str_[i]
                else:
                    break
            if new_str == "+" or new_str == "-":
                return 0
        elif str_[0].isdigit():
            new_str = ""
            for i in range(0, len(str_)):
                if str_[i].isdigit():
                    new_str += str_[i]
                else:
                    break
        else:
            return 0

        n = int(new_str)
        if n < -2 ** 31:
            return -2 ** 31
        elif n > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return n
