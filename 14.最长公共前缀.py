#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start

# Tips: string

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_len = min(len(each_str) for each_str in strs)
        pre = ""
        for i in range(0, min_len):
            c = strs[0][i]
            for each_str in strs:
                if c != each_str[i]:
                    return pre
            pre = pre + c

        return pre

# @lc code=end

