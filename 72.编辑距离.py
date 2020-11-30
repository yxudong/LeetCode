#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start

#Tips: string, dynamic-programming

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 本质不同的操作实际上只有三种：
        #     1. 在单词 A 中插入一个字符；
        #     2. 在单词 B 中插入一个字符；
        #     3. 修改单词 A 的一个字符

        # 当获得 D[i][j-1]，D[i-1][j] 和 D[i-1][j-1] 的值之后就可以计算出 D[i][j]
        #     1. D[i][j-1] 为 A 的前 i 个字符和 B 的前 j - 1 个字符编辑距离的子问题
        #     即对于 B 的第 j 个字符，在 A 的末尾添加了一个相同的字符，那么 D[i][j] 最小可以为 D[i][j-1] + 1；
        #     2. D[i-1][j] 为 A 的前 i - 1 个字符和 B 的前 j 个字符编辑距离的子问题
        #     即对于 A 的第 i 个字符，在 B 的末尾添加了一个相同的字符，那么 D[i][j] 最小可以为 D[i-1][j] + 1；
        #     3. D[i-1][j-1] 为 A 前 i - 1 个字符和 B 的前 j - 1 个字符编辑距离的子问题
        #     即对于 B 的第 j 个字符，修改 A 的第 i 个字符使它们相同，那么 D[i][j] 最小可以为 D[i-1][j-1] + 1
        #     特别地，如果 A 的第 i 个字符和 B 的第 j 个字符原本就相同，那么实际上不需要进行修改操作
        #     在这种情况下，D[i][j] 最小可以为 D[i-1][j-1]

        # 可以写出如下的状态转移方程：
        # 若 A 和 B 的最后一个字母相同：
        #     D[i][j] = min(D[i][j−1] + 1, D[i−1][j] + 1, D[i−1][j−1])
        # 若 A 和 B 的最后一个字母不同：
        #     D[i][j] = min(D[i][j−1] + 1, D[i−1][j] + 1, D[i−1][j−1] + 1)

        m = len(word1)
        n = len(word2)
        # 有一个字符串为空串
        if n * m == 0:
            return n + m

        # D[i][j] 表示 A 的前 i 个字母和 B 的前 j 个字母之间的编辑距离
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # 初始化 dp 数组
        # 对于边界情况，一个空串和一个非空串的编辑距离为 D[i][0] = i 和 D[0][j] = j
        # D[i][0] 相当于对 word1 执行 i 次删除操作，D[0][j] 相当于对 word1执行 j 次插入操作
        for i in range(0, n + 1):
            dp[i][0] = i

        for j in range(0, m + 1):
            dp[0][j] = j

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = dp[i][j - 1]
                up = dp[i - 1][j]
                left_up = dp[i - 1][j - 1]
                if word1[j - 1] == word2[i - 1]:
                    # 若 A 和 B 的最后一个字母相同
                    dp[i][j] = min(left + 1, up + 1, left_up)
                else:
                    # 若 A 和 B 的最后一个字母不同
                    dp[i][j] = min(left + 1, up + 1, left_up + 1)

        return dp[-1][-1]

# @lc code=end

