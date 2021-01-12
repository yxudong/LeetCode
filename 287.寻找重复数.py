#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start

# Tips: array, two-pointers

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 想象成一个环形链表，采用快慢指针方法
        # 将数组下标 n 和数 nums[n] 建立一个映射关系 n -> nums[n] -> nums[nums[n]] -> ...
        # 这样可以把原数组想象成环形链表
        # 首先找到快慢指针在环中的相遇点
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # 再让一个指针从原点出发，一起和环中的相遇点同时向后走一步，相遇时就是环的入口点
        curr = 0
        while curr != slow:
            curr = nums[curr]
            slow = nums[slow]
        return curr

# Tips: array, binary-search

# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         # 采用二分法
#         # 注意这里二分法的 left, right, mid 代表的都是实际值，而不是下标
#         left = 1
#         right = len(nums) - 1
#         while left < right:
#             # 计算出值域的中值
#             mid = left + (right - left) // 2

#             # 计算出小于等于 mid 的值的个数
#             count = 0
#             for i in nums:
#                 if i <= mid:
#                     count = count + 1

#             # 正常情况下，如果没有重复的数字，count 应该等于 mid
#             # 如果大于 mid，说明在 mid 的左边多了几个数字，使得 count > mid
#             # 如果小于等于 mid，说明在 mid 的右边多了几个数字，使得 count > mid
#             if count > mid:
#                 right = mid
#             else:
#                 left = mid + 1

#         return left

# @lc code=end

