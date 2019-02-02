class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        l, s = len(strs), ""
        minl = len(min(strs))
        
        for i in range(0, minl):
            flag = 1
            j = 0
            while j < l -1:
                if strs[j] and strs[j][i] != strs[j+1][i]:
                    flag = 0
                    break
                j += 1
            if flag:
                s += strs[j][i]
            else:
                break
        return s


##############################################################################################


class Solution:
    def longestCommonPrefix(self, m):
        if not m: 
            return ""

        s1 = min(m)
        s2 = max(m)

        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]
        return s1


##############################################################################################


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
            
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]

        return min(strs)

