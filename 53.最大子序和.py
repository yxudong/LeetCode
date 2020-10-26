#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start

# Tips: array, dynamic-programming

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_num = nums[0]
        tmp_sum = max_num
        for i in range(1, len(nums)):
            if tmp_sum > 0:
                tmp_sum = tmp_sum + nums[i]
            else:
                tmp_sum = nums[i]
            max_num = max(tmp_sum, max_num)

        return max_num

# @lc code=end

