class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        max = 1
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if self.isunique(s, i, j) and j-i+1 > max:
                    max = j-i+1
        return max

    # return true if the characters in the substring are all unique, otherwise false
    def isunique(self, s, start, end):
        unique = set(s[start:end+1])
        if len(unique) == end - start + 1:
            return True
        else:
            return False


##############################################################################################


class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        maxn, i, j = 1, 0, 0
        newset = set()
        while i < len(s) and j < len(s):
            if s[j] not in newset:
                newset.add(s[j])
                j += 1
                if j-i > maxn:
                    maxn = j-i
            else:
                newset.remove(s[i])
                i += 1
        return maxn


##############################################################################################


class Solution:
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength