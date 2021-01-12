#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start

# Tips: depth-first-search

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(_i, _j):
            grid[_i][_j] = "0"
            neighbor = [(_i - 1, _j), (_i + 1, _j), (_i, _j - 1), (_i, _j + 1)]
            for ii, jj in neighbor:
                if 0 <= ii < length_h and 0 <= jj < length_w:
                    if grid[ii][jj] == "1":
                        dfs(ii, jj)

        count = 0
        length_h = len(grid)
        length_w = len(grid[0])
        for i in range(0, length_h):
            for j in range(0, length_w):
                if grid[i][j] == "1":
                    # 遇到一次 "1" 时数量加 1，每次遇到一个 "1"，会把相连的 "1" 都设置为 "0"
                    count = count + 1
                    # 这个函数会把和 (i, j) 相连的 "1" 都设置为 "0"
                    dfs(i, j)

        return count

# Tips: breadth-first-search

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         count = 0
#         queue = []
#         length_h = len(grid)
#         length_w = len(grid[0])
#         for i in range(0, length_h):
#             for j in range(0, length_w):
#                 if grid[i][j] == "1":
#                     # 遇到一次 "1" 时数量加 1，每次遇到一个 "1"，会把相连的 "1" 都设置为 "0"
#                     count = count + 1
#                     # 把广度优先遍历初始的点加入队列
#                     queue.append((i, j))
#                     while queue:
#                         # 从队列里面依次弹出元素
#                         tmp_i, tmp_j = queue.pop(0)
#                         if grid[tmp_i][tmp_j] == "1":
#                             # 如果弹出的元素是 "1"，设置为 "0"，并且把相邻的点加入队列
#                             grid[tmp_i][tmp_j] = "0"
#                             neighbor = [(tmp_i - 1, tmp_j), (tmp_i + 1, tmp_j),
#                                         (tmp_i, tmp_j - 1), (tmp_i, tmp_j + 1)]
#                             for ii, jj in neighbor:
#                                 if 0 <= ii < length_h and 0 <= jj < length_w:
#                                     queue.append((ii, jj))

#         return count

# @lc code=end

