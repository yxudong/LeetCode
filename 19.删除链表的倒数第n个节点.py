#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Tips: linked-list

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head

        front_node = head
        curr_node = head
        while n > 0:
            front_node = front_node.next
            n = n - 1

        while front_node and front_node.next:
            front_node = front_node.next
            curr_node = curr_node.next

        if curr_node == head and not front_node:
            return head.next
        curr_node.next = curr_node.next.next
        return head

# @lc code=end

