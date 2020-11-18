#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start

# Tips: string, two-pointers

class Solution:
    def countSubstrings(self, s: str) -> int:
        # 以 i, j 为中心向两边扩张，计算出以 i, j 为中心的回文字符串有多少个
        def get_center_count(s, i, j):
            count = 0
            while i <= j and i >= 0 and j <= length - 1:
                if s[i] == s[j]:
                    count = count + 1
                    i = i - 1
                    j = j + 1
                else:
                    break

            return count

        length = len(s)
        total_count = 0
        for idx in range(0, length):
            # 计算出以 idx 为中心的情况有多少个（子串字符有奇数个）
            count1 = get_center_count(s, idx, idx)
            total_count = total_count + count1
            # 计算出以 idx， idx + 1 为中心的情况有多少个（子串字符有偶数个）
            count2 = get_center_count(s, idx, idx + 1)
            total_count = total_count + count2

        return total_count

# @lc code=end

