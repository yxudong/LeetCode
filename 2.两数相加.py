#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Tips: linked-list

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        jw = 0
        result = []
        while l1 or l2:
            num1 = 0 if l1 == None else l1.val
            num2 = 0 if l2 == None else l2.val
            one_sum = num1 + num2 + jw
            jw = 0
            if one_sum >= 10:
                one_sum = one_sum - 10
                jw = 1
            result.append(one_sum)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if jw == 1:
            result.append(1)

        result_node = ListNode(result[0])
        node_tmp = result_node
        for i in range(1, len(result)):
            node_tmp.next = ListNode(result[i])
            node_tmp = node_tmp.next
        return result_node

# @lc code=end

