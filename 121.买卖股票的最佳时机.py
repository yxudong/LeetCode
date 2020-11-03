#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start

#Tips: array, dynamic-programming

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        # 记录历史最低价格 in_min
        in_min = prices[0]
        max_profit = 0
        for price in prices:
            # 在第 i 天卖出股票的利润是 prices[i] - in_min
            # 比较是否超过最大利润
            max_profit = max(price - in_min, max_profit)
            in_min = min(in_min, price)

        return max_profit

# @lc code=end

