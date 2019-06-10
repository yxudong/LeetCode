class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        minl = len(min(strs, key=len))
        s = ""
        for i in range(minl):
            c = strs[0][i]
            flag = 1
            for j in range(1, len(strs)):
                if strs[j][i] != c:
                    flag = 0
                    break
            if not flag:
                break
            s += c
        return s


##############################################################################################


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
            
        for i, letter_group in enumerate(zip(*strs)):
        # strs = ["flower","flow","flight"] 时
        # list(zip(*strs)) 为 [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]
            if len(set(letter_group)) > 1:
                return strs[0][:i]

        return min(strs)
