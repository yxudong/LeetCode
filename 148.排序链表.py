#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Tips: linked-list, sort

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 使用迭代方式的归并排序

        # 合并两个链表的函数
        def merge(_head1, _head2):
            _dummy_head = ListNode(0)
            _curr, tmp1, tmp2 = _dummy_head, _head1, _head2
            while tmp1 and tmp2:
                if tmp1.val < tmp2.val:
                    _curr.next = tmp1
                    tmp1 = tmp1.next
                else:
                    _curr.next = tmp2
                    tmp2 = tmp2.next
                _curr = _curr.next
            if tmp1:
                _curr.next = tmp1
            if tmp2:
                _curr.next = tmp2

            return _dummy_head.next

        # 统计出链表的长度
        length = 0
        tmp = head
        while tmp:
            length = length + 1
            tmp = tmp.next

        dummy_head = ListNode(0, head)
        # 1. sub_length 表示每次需要排序的子链表的长度，初始时 sub_length = 1
        # 2. 每次将链表拆分成若干个长度为 sub_length 的子链表（最后一个子链表的长度可以小于 sub_length）
        #    按照每两个子链表一组进行合并
        #    合并后即可得到若干个长度为 sub_length * 2 的有序子链表（最后一个子链表的长度可以小于 sub_length * 2）
        # 3. 将 sub_length 的值加倍，重复第 2 步，对更长的有序子链表进行合并操作，直到有序子链表的长度大于或等于 length
        sub_length = 1
        while sub_length < length:
            pre = dummy_head
            # curr 表示当前处理到哪里
            curr = dummy_head.next
            while curr:
                # 获取 head1
                head1 = curr
                for _ in range(1, sub_length):
                    if curr.next:
                        curr = curr.next
                    else:
                        break
                # 获取 head2
                head2 = curr.next
                curr.next = None
                curr = head2
                for _ in range(1, sub_length):
                    # 这里 curr 可能为 None，所以多判断一下
                    if curr and curr.next:
                        curr = curr.next
                    else:
                        break

                # 记录下 curr.next，这里 curr 也可能为 None
                succ = None
                if curr:
                    succ = curr.next
                    curr.next = None

                # 合并两个链表
                merged = merge(head1, head2)
                # pre 表示合并后的链表应该放的位置的前结点
                pre.next = merged
                while pre.next:
                    pre = pre.next

                curr = succ

            sub_length = sub_length * 2

        return dummy_head.next

# @lc code=end

