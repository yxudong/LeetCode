#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start

# Tips: two-pointers

class Solution:
    def get_expand_start_end(self, s, left, right):
        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            left = left - 1
            right = right + 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(0, len(s)):
            tmp_start, tmp_end = self.get_expand_start_end(s, i, i)
            if tmp_end - tmp_start > end - start:
                end = tmp_end
                start = tmp_start
            tmp_start, tmp_end = self.get_expand_start_end(s, i, i + 1)
            if tmp_end - tmp_start > end - start:
                end = tmp_end
                start = tmp_start
        return s[start:end + 1]

# @lc code=end

