#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Tips: tree

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 前序遍历访问各结点的顺序是根结点、左子树、右子树
        # 如果一个结点的左子结点为空，则该结点不需要进行展开操作
        # 如果一个结点的左子结点不为空，则该结点的左子树中的最后一个结点被访问之后，该结点的右子结点被访问
        # 该结点的左子树中最后一个被访问的结点是左子树中的最右边的结点，也是该结点右结点的前驱结点
        # 因此，问题转化成寻找当前结点的前驱结点

        # 具体做法是
        # 对于当前结点，如果其左子结点不为空，则在其左子树中找到最右边的结点作为前驱结点
        # 将当前结点的右子结点赋给前驱结点的右子结点
        # 然后将当前结点的左子结点赋给当前结点的右子结点，并将当前结点的左子结点设为空
        # 对当前结点处理结束后，继续处理链表中的下一个结点，直到所有结点都处理结束
        curr = root
        while curr:
            if curr.left:
                # 如果存在左子树
                # 下面三行寻找到左子树的最右结点
                pre = curr.left
                while pre.right:
                    pre = pre.right
                # 左子树的最右结点是当前结点的右结点前驱结点
                # 所以 左子树的最右结点（pre）.right = 当前结点（curr）.right
                pre.right = curr.right
                # 将当前结点的右结点设为当前结点的左子结点
                curr.right = curr.left
                # 将当前结点的左子树设为空，因为此时当前结点连着左子树的这条线已经没有用了
                curr.left = None
            # 将当前结点向右移动
            curr = curr.right

        return root

# @lc code=end

