#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start

# Tips: array, backtracking

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        # 矩阵中只有一个元素时特殊处理，否则下面的程序不能兼容
        if m == 1 and n == 1:
            return board[0][0] == word

        length = len(word)

        # 代表是否使用过
        used = [[0] * n for _ in range(m)]

        def check_is_exist(idx, _i, _j):
            if _i < 0 or _i > m - 1 or _j < 0 or _j > n - 1:
                # 数组越界，说明这个方向不可以
                return False
            if idx == length:
                # 全部检查完毕，符合
                return True
            if word[idx] != board[_i][_j] or (word[idx] == board[_i][_j] and used[_i][_j] == 1):
                # 当前值和要找的值不相等 或 虽然值相等，但是这个值已经被用过了
                return False
            # 加入到已用数组中，对应位置置为 1
            used[_i][_j] = 1
            if check_is_exist(idx + 1, _i - 1, _j) or check_is_exist(idx + 1, _i + 1, _j) or \
                    check_is_exist(idx + 1, _i, _j - 1) or check_is_exist(idx + 1, _i, _j + 1):
                # 检查四个方向，有一个方向的值存在说明符合
                return True
            else:
                # 四个方向检查完毕，没有符合条件的值，已用数组中对应位置置为 0
                used[_i][_j] = 0
                return False

        for i in range(0, m):
            for j in range(0, n):
                if check_is_exist(0, i, j):
                    return True

        return False

# @lc code=end

