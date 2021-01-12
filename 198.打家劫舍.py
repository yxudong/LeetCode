#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start

# Tips: array, dynamic-programming

class Solution:
    def rob(self, nums: List[int]) -> int:
        # 动态数组 dp 可以优化，达到空间复杂度 O（1）
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        pre, curr = nums[0], max(nums[0], nums[1])
        for i in range(2, length):
            # 随着 i 向前遍历一位
            # 此时 pre 对应 dp 数组 i 的前两位，curr 对应 dp 数组 i 的前一位
            pre, curr = curr, max(curr, pre + nums[i])

        return curr

# Tips: array, dynamic-programming

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         length = len(nums)
#         if length == 0:
#             return 0
#         if length == 1:
#             return nums[0]
#         # dp[i] 代表前 i 间房子能偷到的最高总金额
#         dp = [0] * length
#         # 有一个房子，偷这个房子即可
#         dp[0] = nums[0]
#         # 有两个房子，偷两个中最大的一个
#         dp[1] = max(nums[0], nums[1])
#         for i in range(2, length):
#             # 对于第 k(k>2) 间房子，有两个选项：
#             # 1. 偷第 k 间房子，那么就不能偷第 k-1 间房子
#             #    偷窃总金额为前 k-2 间房子的最高总金额和第 k 间房子的金额之和
#             # 2. 不偷第 k 间房子，偷窃总金额为前 k-1 间房子的最高总金额
#             dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

#         return dp[-1]

# @lc code=end

