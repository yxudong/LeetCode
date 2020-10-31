#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        ans_list = []
        queue = [root]
        while queue:
            tmp_list = []
            for _ in range(0, len(queue)):
                tmp_node = queue.pop(0)
                tmp_list.append(tmp_node.val)
                if tmp_node.left:
                    queue.append(tmp_node.left)
                if tmp_node.right:
                    queue.append(tmp_node.right)
            ans_list.append(tmp_list)

        return ans_list

# @lc code=end

