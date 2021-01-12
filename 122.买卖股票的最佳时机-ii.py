#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start

# Tips: array, dynamic-programming

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        # dp[i][0] 表示第 i 天交易完成手中不持有股票的最大金额数，出现这样的情况可能是：
        #     第 i-1 天不持有股票，第 i 天无交易；
        #     第 i-1 天持有股票，但是第 i 天将其卖出，获取利润
        #     那么 dp[i][0] 的转移方程如下：
        #         dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        # dp[i][1] 表示第 i 天交易完成后手中持有一只股票的最大金额数，同样可能出现的情况如下：
        #     第 i-1 天持有股票，第 i 天无交易；
        #     第 i-1 天不持有股票，第 i 天买入
        #     此时 dp[i][1] 的转移方程如下：
        #         dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        dp = [[0, 0] for _ in range(length)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, length):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])

        return dp[-1][0]

# Tips: array, dynamic-programming

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         # 在上面的方法中，当天的状态值只与前一天的状态值有关
#         # 可以进行优化，用两个变量来存储前一天的状态值，用以计算后面一天状态值
#         # 然后去维护更新这两个变量
#         length = len(prices)
#         dp0 = 0
#         dp1 = -prices[0]
#         for i in range(1, length):
#             dp0 = max(dp0, dp1 + prices[i])
#             dp1 = max(dp1, dp0 - prices[i])

#         return dp0

# Tips: array, greedy

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         length = len(prices)
#         sum_money = 0
#         for i in range(1, length):
#             sum_money = sum_money + max(0, prices[i] - prices[i-1])

#         return sum_money

# @lc code=end

