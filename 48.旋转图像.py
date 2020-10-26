#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range(0, length):
            for j in range(i, length):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(0, length):
            matrix[i].reverse()

        return

# @lc code=end

