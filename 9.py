class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revertnum = 0
        while x > revertnum:
            revertnum = revertnum * 10 + x % 10
            x = int(x / 10)

        return (x == revertnum or x == int(revertnum / 10))