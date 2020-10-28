#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start

# Tips: array, two-pointers, sort

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        # left 代表 0 的右边界
        # right 代表 2 的左边界
        i, left, right = 0, 0, length - 1
        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                i = i + 1
                left = left + 1
            elif nums[i] == 1:
                i = i + 1
            else:
                nums[i], nums[right] = nums[right], nums[i]
                right = right - 1
        return

# @lc code=end

