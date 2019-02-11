class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        news = ""
        if numRows == 1:
            return s
        
        step = (numRows - 1) * 2
        n = len(s)
        for i in range(numRows):
            if i == 0:
                j = 0
                while j < n:
                    news += s[j]
                    j += step
            elif i == numRows - 1:
                j = numRows - 1
                while j < n:
                    news += s[j]
                    j += step
            else:
                j = 0
                while j < n:
                    if j - i >= 0:
                        news += s[j - i]
                    if j + i < n:
                        news += s[j + i]
                    j += step
                if j - step < n - 1 and n - 1 < j and j - i < n:
                    news += s[j - i]
                    
        return news