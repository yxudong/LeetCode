#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Tips: tree, depth-first-search

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return
            left = dfs(node.left)
            right = dfs(node.right)
            node.left = right
            node.right = left
            return node

        return dfs(root)

# Tips: tree, breadth-first-search

# class Solution:
#     def invertTree(self, root: TreeNode) -> TreeNode:
#         if not root:
#             return

#         queue = [root]
#         while queue:
#             node = queue.pop(0)
#             # 每次都从队列中拿一个节点，并交换这个节点的左右子树
#             node.left, node.right = node.right, node.left
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)

#         return root

# @lc code=end

