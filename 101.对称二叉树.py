#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Tips: tree, breadth-first-search

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        queue = [root.left, root.right]
        while queue:
            # 每次从队列里面取两个
            left_node = queue.pop(0)
            right_node = queue.pop(0)
            if not (left_node or right_node):
                # 如果左右两边结点同时都没有，继续
                continue
            if left_node and right_node:
                # 如果左右两边结点同时存在
                if left_node.val != right_node.val:
                    return False
                queue.append(left_node.left)
                queue.append(right_node.right)
                queue.append(left_node.right)
                queue.append(right_node.left)
                continue
            if left_node or right_node:
                # 如果左右两边结点只有一个存在，不对称，返回 False
                return False

        return True

# Tips: tree, recursive, depth-first-search

# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         if not root:
#             return True

#         def dfs(left_node, right_node):
#             if not (left_node or right_node):
#                 # 如果左右两边结点同时都没有，返回 True
#                 return True
#             if left_node and right_node:
#                 # 如果左右两边结点同时存在
#                 if left_node.val != right_node.val:
#                     return False
#                 return dfs(left_node.right, right_node.left) and dfs(left_node.left, right_node.right)
#             if left_node or right_node:
#                 # 如果左右两边结点只有一个存在，不对称，返回 False
#                 return False

#         return dfs(root.left, root.right)

# Tips: tree, recursive, depth-first-search

# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         # 对称二叉树中序遍历出来的列表一定是左右对称的
#         # 但左右对称的列表不一定是对称二叉树
#         # 例如  2
#         #      /
#         #     2
#         #      \
#         #       2
#         # 所以不能完全采用中序遍历判断，可以在中序遍历的列表中加入深度，就完全正确
#         # 例如：res.append((root.val, depth))
#         res = []

#         def in_order(node, depth):
#             if node is None:
#                 return
#             in_order(node.left, depth + 1)
#             res.append((node.val, depth))
#             in_order(node.right, depth + 1)

#         in_order(root, 0)
#         return res == res[::-1]

# @lc code=end

