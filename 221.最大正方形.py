#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start

# Tips: dynamic-programming

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        length_h = len(matrix)
        length_w = len(matrix[0])
        # 用 dp(i, j) 表示以 (i, j) 为右下角，且只包含 1 的正方形的边长最大值
        dp = [[0] * length_w for _ in range(length_h)]
        max_side = 0
        for i in range(length_h):
            for j in range(length_w):
                if matrix[i][j] == "0":
                    # 如果该位置的值是 0，则 dp(i, j) = 0，因为当前位置不可能在由 1 组成的正方形中
                    dp[i][j] = 0
                    continue
                # 如果该位置的值是 1
                if i == 0 or j == 0:
                    # 需要考虑边界条件
                    # 如果 i 和 j 中至少有一个为 0，则以位置 (i, j) 为右下角的最大正方形的边长只能是 1
                    dp[i][j] = 1
                else:
                    # dp(i, j) 的值由其上方、左方和左上方的三个相邻位置的 dp 值决定
                    # 就像 木桶的短板理论 一样，附近的最小边长，才能决定 dp(i, j)
                    # 具体而言，当前位置的元素值等于三个相邻位置的元素中的最小值加 1
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                max_side = max(max_side, dp[i][j])

        return max_side * max_side

# @lc code=end

