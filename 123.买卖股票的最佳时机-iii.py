#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start

# Tips: array, dynamic-programming

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        # dp[i][j][k]，i 表示第几天，j 表示当天结束是否持有股票，k 表示卖出股票的次数
        dp = [[[0, 0, 0], [0, 0, 0]] for _ in range(length)]
        dp[0][0][0] = 0
        dp[0][0][1] = float("-inf")
        dp[0][0][2] = float("-inf")
        dp[0][1][0] = -prices[0]
        dp[0][1][1] = float("-inf")
        for i in range(1, length):
            dp[i][0][0] = dp[i-1][0][0]
            dp[i][0][1] = max(dp[i-1][0][1], dp[i-1][1][0] + prices[i])
            dp[i][0][2] = max(dp[i-1][0][2], dp[i-1][1][1] + prices[i])
            dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][0][0] - prices[i])
            dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][1] - prices[i])

        return max(dp[-1][0][1], dp[-1][0][2], 0)

# @lc code=end

