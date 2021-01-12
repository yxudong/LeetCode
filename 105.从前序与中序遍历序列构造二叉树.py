#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Tips：array, tree, depth-first-search

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(preorder, pre_left, pre_right, inorder, in_left, in_right):
            if pre_left > pre_right or in_left > in_right:
                return
            # # 下面的判断可以节省一次递归，但是不加不影响最终结果
            # if pre_left == pre_right:
            #     return TreeNode(preorder[pre_left])
            # 前序的第一个结点一定是当前子树的根结点
            tmp_root_data = preorder[pre_left]
            root = TreeNode(tmp_root_data)
            # 查找结点在中序的位置，可以使用哈希表优化查找
            in_root_idx = inorder.index(tmp_root_data)
            root.left = build(preorder, pre_left + 1, pre_left + in_root_idx - in_left, inorder, in_left, in_root_idx - 1)
            root.right = build(preorder, pre_left + in_root_idx - in_left + 1, pre_right, inorder, in_root_idx + 1, in_right)
            return root
        
        return build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

# @lc code=end

