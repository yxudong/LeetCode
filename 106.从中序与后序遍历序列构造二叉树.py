#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Tips: array, tree, depth-first-search

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(inorder, in_left, in_right, postorder, post_left, post_right):
            if in_left > in_right or post_left > post_right:
                return
            # # 下面的判断可以节省一次递归，但是不加不影响最终结果
            # if post_left == post_right:
            #     return TreeNode(postorder[post_left])
            # 后序的最后一个结点一定是当前子树的根结点
            tmp_root_data = postorder[post_right]
            root = TreeNode(tmp_root_data)
            # 查找结点在中序的位置，可以使用哈希表优化查找
            in_root_idx = inorder.index(tmp_root_data)
            root.left = build(inorder, in_left, in_root_idx - 1, postorder, post_left, post_left + in_root_idx - in_left - 1)
            root.right = build(inorder, in_root_idx + 1, in_right, postorder, post_left + in_root_idx - in_left, post_right - 1)
            return root
        
        return build(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)

# @lc code=end

