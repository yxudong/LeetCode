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
        if m == 1 and n == 1:
            return board[0][0] == word

        length = len(word)
        used = [[0] * n for _ in range(m)]

        def check_is_exist(idx, _i, _j):
            if _i < 0 or _i > m - 1 or _j < 0 or _j > n - 1:
                return False
            if idx == length:
                return True
            if word[idx] != board[_i][_j] or (word[idx] == board[_i][_j] and used[_i][_j] == 1):
                return False
            used[_i][_j] = 1
            if check_is_exist(idx + 1, _i - 1, _j) or check_is_exist(idx + 1, _i + 1, _j) or \
                    check_is_exist(idx + 1, _i, _j - 1) or check_is_exist(idx + 1, _i, _j + 1):
                return True
            else:
                used[_i][_j] = 0
                return False

        for i in range(0, m):
            for j in range(0, n):
                if check_is_exist(0, i, j):
                    return True

        return False

# @lc code=end

