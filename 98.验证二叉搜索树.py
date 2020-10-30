#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Tips: tree, stack, depth-first-search

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 二叉搜索树「中序遍历」得到的值构成的序列一定是升序的
        # 非递归中序遍历
        pre = float("-inf")
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            tmp_node = stack.pop()
            if tmp_node.val <= pre:
                return False
            pre = tmp_node.val
            root = tmp_node.right

        return True

#Tips: tree, recursive

# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         def dfs(node, lower=float('-inf'), upper=float('inf')):
#             if not node:
#                 return True
#             # 下面这个判断可以放在任意位置，不需要管前中后序
#             if node.val <= lower or node.val >= upper:
#                 return False
#             if not dfs(node.left, lower, node.val):
#                 return False
#             if not dfs(node.right, node.val, upper):
#                 return False
#             return True

#         return dfs(root)

#Tips: tree, recursive, depth-first-search

# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         # 二叉搜索树「中序遍历」得到的值构成的序列一定是升序的
#         # 递归中序遍历
#         pre = float('-inf')

#         def dfs(node):
#             if not node:
#                 return True
#             if not dfs(node.left):
#                 return False
#             # 加 nonlocal 关键字引用和修改外部变量，否则不能引用和修改 pre
#             nonlocal pre
#             if node.val <= pre:
#                 return False
#             pre = node.val
#             if not dfs(node.right):
#                 return False
#             return True

#         return dfs(root)

# @lc code=end

