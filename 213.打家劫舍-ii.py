#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start

# Tips: array, dynamic-programming

class Solution:
    def rob(self, nums: List[int]) -> int:
        def one_rob(array):
            sub_length = len(array)
            if sub_length == 0:
                return 0
            if sub_length == 1:
                return array[0]
            dp = [0] * sub_length
            dp[0] = array[0]
            dp[1] = max(array[0], array[1])
            for i in range(2, sub_length):
                dp[i] = max(dp[i-1], dp[i-2] + array[i])

            return dp[-1]

        length = len(nums)
        if length == 1:
            return nums[0]
        return max(one_rob(nums[1:]), one_rob(nums[:-1]))

# @lc code=end

