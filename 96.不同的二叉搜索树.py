#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start

#Tips: tree, dynamic-programming

class Solution:
    def numTrees(self, n: int) -> int:
        """
        假设 n 个节点存在二叉排序树的个数是 G (n)
        f(i) 为以 i 为根的二叉搜索树的个数，则
        G(n) = f(1) + f(2) + f(3) + f(4) + ... + f(n)

        当 i 为根节点时，其左子树节点个数为 i-1 个，右子树节点为 n-i，
        则 f(i) = G(i-1) * G(n-i)

        综合两个公式可以得到
        G(n) = G(0)*G(n-1)+G(1)*(n-2)+...+G(n-1)*G(0)

        G(n) 函数的值在数学上被称为卡塔兰数
        Cn+1 = 2(2n + 1) * Cn / (n + 2), C0 = 1
        """
        G = [0] * (n + 1)
        G[0] = 1
        G[1] = 1
        for i in range(2, n + 1):
            # 用 i 表示 G 的下标，当前是 G(i)
            for j in range(1, i + 1):
                # 用 j 表示 f 的下标，当前是 f(j) = G(j-1) * G(i-j)
                G[i] += G[j - 1] * G[i - j]

        return G[n]

#Tips: tree, dynamic-programming, recursive

# class Solution:
#     def numTrees(self, n: int) -> int:
#         # 上面的方法可以递归计算，结果虽然正确，但是会超时
#         if n == 0:
#             return 1
#         if n == 1:
#             return 1
#         total = 0
#         for i in range(0, n):
#             total += self.numTrees(i) * self.numTrees(n - 1 - i)
#         return total

#Tips: tree, math

# class Solution:
#     def numTrees(self, n: int) -> int:
#         # 直接计算卡塔兰数 Cn+1 = 2(2n + 1) * Cn / (n + 2), C0 = 1
#         result = 1
#         for i in range(1, n):
#             result = int(2 * (2 * i + 1) * result / (i + 2))
#         return result

# @lc code=end

