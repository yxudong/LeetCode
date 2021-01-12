#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Tips: linked-list, two-pointers

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def find_middle_node(_head):
            # 通过快慢指针找到中间结点
            slow, fast = _head, _head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

            return slow

        def reverse_linked_list(node):
            # 反转链表
            if not node or not node.next:
                return node
            pre = None
            curr = node
            while curr:
                post = curr.next
                curr.next = pre
                pre = curr
                curr = post

            return pre

        if not head or not head.next:
            return True
        if not head.next.next:
            return head.val == head.next.val

        # 如果是 1 -> 2 -> 3 -> 2 -> 1
        # middle_node 是 3
        # 如果是 1 -> 2 -> 3 -> 3 -> 2 -> 1
        # middle_node 是第一个3
        middle_node = find_middle_node(head)
        # 反转后半部分
        reverse_head = reverse_linked_list(middle_node.next)
        # 把前半部分尾结点的 next 置为 None
        middle_node.next = None
        while head and reverse_head:
            if head.val == reverse_head.val:
                head = head.next
                reverse_head = reverse_head.next
            else:
                return False

        # 此时如果链表有偶数个结点，head 和 reverse_head 都为 None
        # 如果链表有奇数个结点，剩下的 head 为链表奇数个结点中最中间的结点，reverse_head 为 None
        # 两种情况都属于回文链表
        return True

# @lc code=end

