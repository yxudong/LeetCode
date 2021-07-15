#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start

# Tips： array, two-pointers

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 使用双指针，左指针指向当前已经处理好的序列的尾部，右指针指向待处理序列的头部。
        # 右指针不断向右移动，每次右指针指向非零数，则将左右指针对应的数交换，同时左指针右移。
        # 注意到以下性质：
        #     1. 左指针左边均为非零数；
        #     2. 右指针左边直到左指针处均为零。
        # 因此每次交换，都是将左指针的零与右指针的非零数交换，且非零数的相对顺序并未改变。
        # [0, 1, 0, 1, 0, 2, 3, 12]
        # [1, 0, 0, 1, 0, 2, 3, 12]
        # [1, 1, 0, 0, 0, 2, 3, 12]
        # ...
        left = 0
        for right in range(len(nums)):
            if nums[right]:
                nums[right], nums[left] = nums[left], nums[right]
                left = left + 1

        return

# @lc code=end

