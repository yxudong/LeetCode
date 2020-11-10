#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans_list = []
        stack = []
        # 代表先前遍历过的点
        prev = None

        while root or stack:
            while root:
                # 一直找到 root 的最左边
                stack.append(root)
                root = root.left

            root = stack.pop()
            if not root.right or root.right == prev:
                # 如果弹出的结点不存在右结点 或 右结点先前已经遍历过
                # 加入到遍历列表
                ans_list.append(root.val)
                # 标记此次遍历的结点为遍历过的结点
                prev = root
                # 把 root 置为 None 是为了下次循环时可以从栈中弹出元素
                root = None
            else:
                # 如果弹出的结点存在右结点并且右结点还没有遍历过
                # 把该结点重新加入栈
                stack.append(root)
                root = root.right

        return ans_list

#Tips: tree, recursive

# class Solution:
#     def postorderTraversal(self, root: TreeNode) -> List[int]:
#         def dfs(node):
#             if not node:
#                 return
#             dfs(node.left)
#             dfs(node.right)
#             ans_list.append(node.val)

#         ans_list = []
#         dfs(root)
#         return ans_list

# @lc code=end

