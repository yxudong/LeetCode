#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Tips: tree, depth-first-search

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # 实现一个简化的函数 get_max(node)，该函数计算二叉树中的一个结点的最大贡献值
        def get_max(node):
            if not node:
                # 空结点的贡献值是 0
                return 0

            # 左结点的贡献值
            left_max = get_max(node.left)
            # 右结点的贡献值
            right_max = get_max(node.right)
            # 如果左结点或右结点的贡献值小于 0，对于最大路径和没有帮助
            # 所以在加的时候需要和 0 比较，小于 0 没必要加
            node_max = node.val + max(left_max, 0) + max(right_max, 0)
            # 更新最大路径和
            self.max_sum = max(node_max, self.max_sum)

            # 返回该结点的贡献值
            # 该结点的贡献值等于该结点的值 + max(左子结点的贡献值，右子结点的贡献值)
            # max(left_max, right_max, 0) 是因为需要计算路径，只能有一条，左或右或左右都不取
            return node.val + max(left_max, right_max, 0)

        self.max_sum = float("-inf")
        get_max(root)
        return self.max_sum

# @lc code=end

