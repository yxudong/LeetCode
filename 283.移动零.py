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
        # 两个指针，j 在遇到元素为 0 时会停顿，i 继续向前走
        # 遇到非 0 时，i 和 j 的元素交换，并且同时加 1，交换过后，j 指向的还是 0 的位置
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j = j + 1

        return

# @lc code=end

