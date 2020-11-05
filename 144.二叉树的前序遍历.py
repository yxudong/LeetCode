#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Tips: tree, stack

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        ans_list = []

        while root or stack:
            while root:
                # 一直找到 root 的最左边
                stack.append(root)
                # 与非递归中序遍历的区别是加入栈的时候输出
                ans_list.append(root.val)
                root = root.left

            tmp_node = stack.pop()
            root = tmp_node.right

        return ans_list

#Tips: tree, recursive

# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         def dfs(node):
#             if not node:
#                 return
#             ans_list.append(node.val)
#             dfs(node.left)
#             dfs(node.right)

#         ans_list = []
#         dfs(root)
#         return ans_list

# @lc code=end

