#
# @lc app=leetcode.cn id=237 lang=python3
#
# [237] 删除链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Tips: linked-list

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 从链表里删除一个节点 node 的最常见方法是修改之前节点的 next 指针，使其指向之后的节点
        # 因为无法访问想要删除的节点之前的节点，所以不能修改该节点的 next 指针
        # 具体做法是将想要删除的节点的值替换为它后面节点中的值，然后删除它之后的节点
        # 因为要删除的节点不是列表的末尾，所以可以保证这种方法是可行的
        node.val = node.next.val
        node.next = node.next.next
        return
        
# @lc code=end

