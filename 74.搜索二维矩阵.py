#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start

# Tips: array, binary-search

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            mid_num = matrix[mid // n][mid - (mid // n) * n]
            if mid_num == target:
                return True
            elif mid_num > target:
                right = mid - 1
            else:
                left = mid + 1

        return False

# @lc code=end

