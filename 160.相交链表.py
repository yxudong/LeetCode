#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Tips: linked-list

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 先在长的链表走多出的一段距离，然后一起走
        length_a, length_b = 0, 0
        tmp_a, tmp_b = headA, headB
        while tmp_a:
            length_a = length_a + 1
            tmp_a = tmp_a.next
        while tmp_b:
            length_b = length_b + 1
            tmp_b = tmp_b.next
        diff = length_a - length_b
        long_list = headA if diff >= 0 else headB
        short_list = headA if diff < 0 else headB
        diff = abs(diff)
        while diff:
            long_list = long_list.next
            diff = diff - 1
        while long_list != short_list:
            long_list = long_list.next
            short_list = short_list.next

        return long_list

# Tips: linked-list

# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         # 一个链表走到结尾继续走另一个链表，a + c + b = b + c + a
#         tmp_a, tmp_b = headA, headB
#         while tmp_a != tmp_b:
#             # 如果没有相交点，最后是 None = None
#             tmp_a = tmp_a.next if tmp_a else headB
#             tmp_b = tmp_b.next if tmp_b else headA

#         return tmp_a

# @lc code=end

