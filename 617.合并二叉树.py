#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Tips: tree, depth-first-search

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # 采用先序遍历的思想
        if not t1:
            return t2
        if not t2:
            return t1

        # 此时 t1 和 t2 都存在，新建一个结点
        node = TreeNode(t1.val + t2.val)
        node.left = self.mergeTrees(t1.left, t2.left)
        node.right = self.mergeTrees(t1.right, t2.right)
        return node

#Tips: tree, breadth-first-search

# class Solution:
#     def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
#         if not t1:
#             return t2
#         if not t2:
#             return t1

#         new_root = TreeNode(t1.val + t2.val)
#         # 队列 queue 用于新的树
#         queue = [new_root]
#         # 队列 queue1 用于树 t1
#         queue1 = [t1]
#         # 队列 queue2 用于树 t2
#         queue2 = [t2]
#         while queue1 and queue2:
#             node = queue.pop(0)
#             node1 = queue1.pop(0)
#             node2 = queue2.pop(0)
#             if node1.left and node2.left:
#                 new_left_node = TreeNode(node1.left.val + node2.left.val)
#                 node.left = new_left_node
#                 queue.append(new_left_node)
#                 queue1.append(node1.left)
#                 queue2.append(node2.left)
#             elif node1.left:
#                 # 这里不能新建结点
#                 # 因为 t1 或 t2 某棵树 left 不存在时，不会加到队列里，while 循环会终止
#                 # 下面的情况类似
#                 node.left = node1.left
#             elif node2.left:
#                 node.left = node2.left
#             else:
#                 pass

#             if node1.right and node2.right:
#                 new_right_node = TreeNode(node1.right.val + node2.right.val)
#                 node.right = new_right_node
#                 queue.append(new_right_node)
#                 queue1.append(node1.right)
#                 queue2.append(node2.right)
#             elif node1.right:
#                 node.right = node1.right
#             elif node2.right:
#                 node.right = node2.right
#             else:
#                 pass

#         return new_root

# @lc code=end

