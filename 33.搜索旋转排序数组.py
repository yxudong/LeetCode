#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start

# Tips: array, binary-search

class Solution:
    def search(self, nums, target: int) -> int:
        length = len(nums)
        left, right = 0, length - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[length - 1]:
                    left = mid + 1
                else:
                    right = mid - 1

        if nums[left] == target:
            return left

        return -1

# @lc code=end

