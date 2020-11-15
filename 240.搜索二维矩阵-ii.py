#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start

#Tips: array

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 从左下角开始搜索
        # 如果当前指向的值大于目标值，则可以 “向上” 移动一行
        # 否则，如果当前指向的值小于目标值，则可以移动一列
        # 因为行是从左到右排序的，所以当前值右侧的每个值都较大
        # 因此，如果当前值已经大于目标值，我们知道它右边的每个值会比较大。
        # 也可以对列进行非常类似的论证，因此这种搜索方式将始终在矩阵中找到目标（如果存在）。
        row = len(matrix) - 1
        col = 0
        while 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row = row - 1
            else:
                col = col + 1

        return False

# @lc code=end

