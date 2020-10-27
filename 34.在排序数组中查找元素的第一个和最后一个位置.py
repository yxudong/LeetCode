#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start

# Tips: array, binary-search

class Solution:
    def searchRange(self, nums, target: int):
        def find_left_idx(_nums, _target):
            length = len(_nums)
            left, right = 0, length - 1
            while left < right:
                mid = (left + right) // 2
                if _nums[mid] == target:
                    right = mid - 1
                elif _nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            if nums[left] == target:
                return left
            if left < length - 1 and nums[left + 1] == target:
                return left + 1

            return -1

        def find_right_idx(_nums, _target):
            length = len(_nums)
            left, right = 0, length - 1
            while left < right:
                mid = (left + right) // 2
                if _nums[mid] == target:
                    left = mid + 1
                elif _nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            if nums[right] == target:
                return right
            if right > 0 and nums[right - 1] == target:
                return right - 1

            return -1

        if not nums:
            return [-1, -1]

        left_idx = find_left_idx(nums, target)
        if left_idx == -1:
            return [-1, -1]
        right_idx = find_right_idx(nums, target)
    
        return [left_idx, right_idx]

# @lc code=end

