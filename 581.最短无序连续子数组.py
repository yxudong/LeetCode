#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] 最短无序连续子数组
#

# @lc code=start

#Tips: array

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        length = len(nums)
        # 排除掉特殊情况
        if length <= 1:
            return 0

        # 从前向后遍历，使用 max_num，保存到当前位置为止的最大值
        # 如果下个数大于等于 max_num，则更新 max_num
        # 否则，更新需要排序数组的右界 right
        # 起始时右界从 0 开始
        right = 0
        max_num = nums[right]
        for i in range(0, length):
            if nums[i] >= max_num:
                # 注意这里必须是 >=，因为遇到相等的数也要向后移动
                max_num = nums[i]
            else:
                right = i

        # 从后向前遍历，使用 min_num，保存到当前位置为止的最小值
        # 如果下个数小于等于 min_num，则更新 min_num
        # 否则，更新需要排序数组的左界 left
        # 起始时左界从 length - 1 开始
        left = length - 1
        min_num = nums[left]
        for j in range(length - 1, -1, -1):
            if nums[j] <= min_num:
                # 注意这里必须是 <=，因为遇到相等的数也要向前移动
                min_num = nums[j]
            else:
                left = j

        # (right - left + 1) <= 0 说明输入的数组已经是有序的，不存在子数组
        return right - left + 1 if (right - left + 1) > 0 else 0

#Tips: array, sort

# class Solution:
#     def findUnsortedSubarray(self, nums: List[int]) -> int:
#         # 先对数组进行排序，左右指针比较不同的位置
#         new_nums = sorted(nums)
#         start, end = -1, -1
#         for i in range(0, len(nums)):
#             if nums[i] != new_nums[i]:
#                 start = i
#                 break
#         for j in range(len(nums) - 1, -1, -1):
#             if nums[j] != new_nums[j]:
#                 end = j
#                 break

#         if start == end:
#             return 0

#         return end - start + 1

# @lc code=end

