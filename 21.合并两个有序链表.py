#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Tips: linked-list

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_head = ListNode(0)
        tmp_node = new_head
        while l1 and l2:
            if l1.val < l2.val:
                tmp_node.next = ListNode(l1.val)
                l1 = l1.next
            else:
                tmp_node.next = ListNode(l2.val)
                l2 = l2.next
            tmp_node = tmp_node.next

        if l1:
            tmp_node.next = l1
        if l2:
            tmp_node.next = l2

        return new_head.next

# @lc code=end

