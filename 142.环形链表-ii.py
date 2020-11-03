#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Tips: linked-list, two-pointers

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return
        # 1. 首先找到环中相遇点
        slow, fast = head, head.next
        while slow != fast:
            if not fast or not fast.next:
                return
            slow = slow.next
            fast = fast.next.next

        # 此时 slow 和 fast 相等，位置为环中相遇点
        # 以 [3] -> [2] -> [0] -> [-4] -> [2] 举例，此时 slow 和 fast 同时位于 [0]
        # 从相遇点到入环点的距离加上 n - 1 圈的环长，恰好等于从链表头部到入环点的距离
        # 2. 额外使用一个指针 ptr，指向 head，它和 slow 每次同时向后移动一个位置。最终，它们会在入环点相遇
        ptr = head
        # 这里是为了弥补一个差值，此时 slow 位于 [0]，需要向后移动一个位置到 [-4]，才可以刚好和 ptr 在入环点相遇
        # 否则下面的 while 会陷入死循环
        slow = slow.next
        while slow != ptr:
            slow = slow.next
            ptr = ptr.next

        return ptr
        
# @lc code=end

