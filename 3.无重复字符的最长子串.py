#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start

# Tips: sliding-window, two-pointers

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_s = len(s)
        if len_s <= 1:
            return len_s

        max_sub_len, right_point = 1, 1
        set_s = set()
        set_s.add(s[0])
        for left_point in range(0, len_s):
            while right_point < len_s:
                if s[right_point] not in set_s:
                    set_s.add(s[right_point])
                    right_point = right_point + 1
                    max_sub_len = max(max_sub_len, right_point - left_point)
                else:
                    set_s.remove(s[left_point])
                    break

        return max_sub_len

# @lc code=end

