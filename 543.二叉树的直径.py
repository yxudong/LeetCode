#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Tips: tree, recursive

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 代表直径上的结点数
        self.diameter_node = 1
        def get_depth_dfs(node):
            if not node:
                return 0
            # 左儿子为根的子树的深度
            left = get_depth_dfs(node.left)
            # 右儿子为根的子树的深度
            right = get_depth_dfs(node.right)
            # 不断比较更新直径上的结点数
            # 以某个结点为根的树 直径上的结点数等于左子树深度 + 右子树深度 + 1
            self.diameter_node = max(left + right + 1, self.diameter_node)
            # 返回该节点为根的子树的深度
            return max(left, right) + 1

        get_depth_dfs(root)
        return self.diameter_node - 1

# @lc code=end

