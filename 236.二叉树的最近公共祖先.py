#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Tips: tree, recursive

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 采用后序遍历
        # 自底向上从叶子节点开始更新，所以在所有满足条件的公共祖先中一定是深度最大的祖先先被访问到
        # root 是 p, q 的最近公共祖先 ，只可能为以下情况之一：
        # 1. p 和 q 在 root 的子树中，且分列 root 的 异侧（即分别在左、右子树中）；
        # 2. p = root，且 q 在 root 的左或右子树中；
        # 3. q = root，且 p 在 root 的左或右子树中；
        if not root:
            return
        if p.val == root.val or q.val == root.val:
            # 属于情况 2, 3
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 1. 当 left 和 right 同时为空：说明 root 的左 / 右子树中都不包含 p,q，返回 None；
        # 2. 当 left 和 right 同时不为空：说明 p, q 分列在 root 的异侧（分别在 左 / 右子树），因此 root 为最近公共祖先，返回 root；
        # 3. 当 left 为空，right 不为空：p,q 都不在 root 的左子树中，直接返回 right。具体可分为两种情况：
        #    3.1 p,q 其中一个在 root 的右子树中，此时 right 指向 p（假设为 p）；
        #    3.2 p,q 两节点都在 root 的右子树中，此时的 right 指向最近公共祖先节点 ；
        # 4. 当 left 不为空，right 为空 ：与情况 3 同理；
        if left and right:
            return root
        if not left:
            return right
        if not right:
            return left

# @lc code=end

