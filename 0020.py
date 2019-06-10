class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in range(0, len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            else:
                if not stack:
                    return False
                pop_s = stack.pop()
                if s[i] == "]":
                    if pop_s != "[":
                        return False
                elif s[i] == ")":
                    if pop_s != "(":
                        return False
                else:
                    if pop_s != "{":
                        return False
        if stack:
            return False
        else:
            return True
