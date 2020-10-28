#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start

# Tips: array, dynamic-programming

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 初始化
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    # 原点
                    continue
                elif i == 0 and j != 0:
                    # 最上面一行
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif i != 0 and j == 0:
                    # 最左边一列
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]

        return grid[-1][-1]

# @lc code=end

