#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start

# Tips: array, dynamic-programming

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 优化空间过后的动态规划方法
        dp = [1] * n
        for _ in range(1, m):
            for i in range(1, n):
                dp[i] = dp[i - 1] + dp[i]

        return dp[-1]

        # # 最原始的动态规划方法

        # dp = [[0] * n for _ in range(m)]

        # # 初始化
        # for i in range(m):
        #     dp[i][0] = 1
        # for i in range(n):
        #     dp[0][i] = 1
        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # return dp[-1][-1]

# Tips: array

# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         # C m+n−2 m−1
#         # (m+n−2)! / (m−1)! / ((m+n−2)-(m-1))!
#         return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))

# @lc code=end

