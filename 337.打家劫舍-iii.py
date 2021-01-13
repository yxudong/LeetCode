#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Tips: tree, depth-first-search, dynamic-programming

class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0, 0

            left1, left2 = dfs(node.left)
            right1, right2 = dfs(node.right)
            if node.left or node.right:
                return node.val + left2 + right2, max(left1, left2) + max(right1, right2)
            else:
                return node.val, 0

        max1, max2 = dfs(root)
        return max(max1, max2)

# @lc code=end

