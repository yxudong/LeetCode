#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start

# Tips: two-pointers

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_area = min(height[i], height[j]) * (j - i)
        while i != j:
            if height[i] < height[j]:
                i = i + 1
            else:
                j = j - 1
            max_area = max(max_area, min(height[i], height[j]) * (j - i))
        return max_area

# @lc code=end

