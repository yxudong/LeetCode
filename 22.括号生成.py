#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start

# Tips: string, backtracking

class Solution:
    def generateParenthesis(self, n: int):
        def back(left, right, path):
            if left == 0 and right == 0:
                ans.append(path)
                return
            if left > 0:
                back(left - 1, right, path + "(")
            if left < right:
                back(left, right - 1, path + ")")

        ans = []
        back(n, n, "")
        return ans

# @lc code=end

