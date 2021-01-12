#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Tips: tree, recursive

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        # 采用 右 -> 中 -> 左 的遍历方式
        def get_sum_tree(node, curr_sum):
            if not node:
                return 0

            right = get_sum_tree(node.right, curr_sum)
            temp = node.val
            curr_sum = curr_sum + right + node.val
            node.val = curr_sum
            left = get_sum_tree(node.left, curr_sum)

            return right + temp + left

        get_sum_tree(root, 0)
        return root

# @lc code=end

