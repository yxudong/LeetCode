class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        if s[0] == "-":
            if len(s) != 2:
                s = "-" + s[-1:0:-1]
            else:
                s = "-" + s[1]
        else:
            s = s[::-1]
        n = int(s)
        if n < -2**31 or n > 2**31 - 1:
            return 0
        else:
            return n

			
			
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        while x != 0:
            pop = int(x % 10)
            x = int(x / 10)
            if rev > int(INT_MAX/10) or (rev == int(INT_MAX / 10) and pop > 7):
                return 0
            if (rev < int(INT_MIN/10) or (rev == int(INT_MIN / 10) and pop < -8)):
                return 0
            rev = rev * 10 + pop
        return rev