#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start

# Tips: string, stack

class Solution:
    def isValid(self, s: str) -> bool:
        # 补充
        ##########################
        if len(s) % 2 == 1:
            return False
        ##########################

        sign_map = {
            "{": "}",
            "(": ")",
            "[": "]",
        }
        stack = []
        if s == "":
            return True
        for i in s:
            if i in ["{", "(", "["]:
                stack.append(i)
            else:
                if not stack:
                    return False
                item = stack.pop()
                if sign_map[item] != i:
                    return False
        if stack:
            return False
        return True

# @lc code=end

