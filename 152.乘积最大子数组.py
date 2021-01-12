#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start

# Tips: array, dynamic-programming

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_min, curr_max = nums[0], nums[0]
        ans_max = nums[0]
        # 遍历数组时计算当前最大值，不断更新
        # 由于存在负数，那么会导致最大的变最小的，最小的变最大的
        # 所以维护两个数，curr_max 为当前最大值，curr_min 为当前最小值
        # curr_max = max(curr_min * nums[i], curr_max * nums[i])
        # curr_min = min(curr_min * nums[i], curr_max * nums[i])
        # 因为有可能出现 0，所以上面的两个比较中加入 nums[i]
        for i in range(1, len(nums)):
            temp_min, temp_max = curr_min, curr_max
            curr_max = max(nums[i], temp_min * nums[i], temp_max * nums[i])
            curr_min = min(nums[i], temp_min * nums[i], temp_max * nums[i])
            ans_max = max(ans_max, curr_max)

        return ans_max

# @lc code=end

