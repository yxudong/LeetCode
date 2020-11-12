#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start

# Tips: quick sort

import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(_array, _left, _right):
            pivot = _left
            while _left < _right:
                # 快速排序升序这样写法一定要先从右边开始找
                # 否则循环终止时 left=right 点的值比 pivot 大，交换会出错误
                while _left < _right and _array[_right] >= _array[pivot]:
                    _right = _right - 1
                while _left < _right and _array[_left] <= _array[pivot]:
                    _left = _left + 1

                _array[_left], _array[_right] = _array[_right], _array[_left]
            _array[_left], _array[pivot] = _array[pivot], _array[_left]

            return _left

        def random_partition(_array, _left, _right):
            # 在原来的 partition 函数上随机选取分隔点，防止极端情况
            random_index = random.randint(_left, _right)
            nums[random_index], nums[_left] = nums[_left], nums[random_index]
            return partition(_array, _left, _right)

        length = len(nums)
        left, right = 0, length - 1
        target_index = length - k
        while True:
            # 每次循环都会有一个元素在排好序的最终位置，循环直到 target_index 位置的值正确
            pivot = random_partition(nums, left, right)
            if pivot == target_index:
                return nums[pivot]
            elif pivot > target_index:
                # 分隔点比目标位置大，从分割点左边开始找
                right = pivot - 1
            else:
                # 分隔点比目标位置小，从分割点右边开始找
                left = pivot + 1

# @lc code=end

