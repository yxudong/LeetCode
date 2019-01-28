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
			
			
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = False
        x_char = str(x)

        "if negative int remove the sign"
        if x_char[0] == '-':
            x_char = x_char[1:]
            flag = True

        "reverse the string"
        rev = x_char[::-1]

        "add the sign if remove before"
        if flag:
            rev = '-' + rev

        "if overflow return 0"
        rev = int(rev)
        if rev > 2**31 - 1 or rev < -2**31:
            rev = 0
        return rev