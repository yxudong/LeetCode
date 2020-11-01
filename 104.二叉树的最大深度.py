#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Tips: tree | depth-first-search

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def get_depth(node):
            if not node:
                return 0
            left_depth = get_depth(node.left)
            right_depth = get_depth(node.right)
            return max(left_depth, right_depth) + 1

        return get_depth(root)

#Tips: tree | breadth-first-search

# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0

#         queue = [root]
#         depth = 0
#         while queue:
#             len_queue = len(queue)
#             for _ in range(0, len_queue):
#                 tmp_node = queue.pop(0)
#                 if tmp_node.left:
#                     queue.append(tmp_node.left)
#                 if tmp_node.right:
#                     queue.append(tmp_node.right)
#             depth = depth + 1

#         return depth

# @lc code=end

