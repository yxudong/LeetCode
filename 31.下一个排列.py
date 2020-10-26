#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start

# Tips: array

class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse_list(_list, start, end):
            while start < end:
                _list[start], _list[end] = _list[end], _list[start]
                start += 1
                end -= 1
            return

        length = len(nums)
        idx = length - 1
        for i in range(length - 1, -1, -1):
            if i == 0:
                reverse_list(nums, 0, length - 1)
                return
            if nums[i - 1] < nums[i]:
                idx = i
                break

        to_swap_num = nums[idx - 1]
        for i in range(length - 1, idx - 1, -1):
            if nums[i] > to_swap_num:
                nums[i], nums[idx - 1] = nums[idx - 1], nums[i]
                break
        reverse_list(nums, idx, length - 1)
        return

# @lc code=end

