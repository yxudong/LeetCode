#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Tips: linked-list

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        curr = head
        while curr:
            post = curr.next
            curr.next = pre
            pre = curr
            curr = post

        return pre

#Tips: linked-list, recursive

# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if not head or not head.next:
#             return head

#         # 把以 head.next 开头的链表反转，返回反转后的头结点
#         node = self.reverseList(head.next)
#         # 假设以 head.next 开头的链表已经反转好了，此时只剩下 head -> head.next
#         # 把 head -> head.next 改成 head.next -> head
#         head.next.next = head
#         # 此时 head 是最后一个结点，head.next 设为 None
#         head.next = None

#         # node 代表反转后的头结点，直接返回
#         return node

# @lc code=end

