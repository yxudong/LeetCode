#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans_list = []
        stack = []

        while root or stack:
            while root:
                # 一直找到 root 的最左边
                stack.append(root)
                root = root.left

            tmp_node = stack.pop()
            # 与非递归前序遍历的区别是弹出栈的时候输出
            ans_list.append(tmp_node.val)
            root = tmp_node.right

        return ans_list

#Tips: tree, recursive

# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         def dfs(_node):
#             if not _node:
#                 return
#             dfs(_node.left)
#             ans_list.append(_node.val)
#             dfs(_node.right)

#         ans_list = []
#         dfs(root)
#         return ans_list
        
# @lc code=end

