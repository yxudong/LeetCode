#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start

# Tips: array, two-pointers

class Solution:
    def trap(self, height: List[int]) -> int:
        # max_left：左边的最大值，它是从左往右遍历找到的
        # max_right：右边的最大值，它是从右往左遍历找到的
        # left：从左往右处理的当前下标
        # right：从右往左处理的当前下标

        # 定理一：在某个位置 i 处，它能存的水，取决于它左右两边的最大值中较小的一个
        # 定理二：当我们从左往右处理到 left 下标时，左边的最大值 max_left 对它而言是可信的，但 max_right 对它而言是不可信的
        # 定理三：当我们从右往左处理到 right 下标时，右边的最大值 max_right 对它而言是可信的，但 max_left 对它而言是不可信的

        # 对于位置 left 而言，它左边最大值一定是 max_left，右边最大值“大于等于” max_right
        # 这时候，如果 max_left < max_right 成立，那么它就知道自己能存多少水了
        # 无论右边将来会不会出现更大的 max_right，都不影响这个结果
        # 所以当 max_left < max_right 时，去处理 left 下标
        # 反之，去处理 right 下标

        if not height:
            return 0

        length = len(height)
        max_left, max_right = height[0], height[length - 1]
        left, right = 0, length - 1
        result = 0
        while left <= right:
            if max_left < max_right:
                max_left = max(max_left, height[left])
                result = result + (max_left - height[left])
                left = left + 1
            else:
                max_right = max(max_right, height[right])
                result = result + (max_right - height[right])
                right = right - 1

        return result

# Tips: array, dynamic-programming

# class Solution:
#     def trap(self, height: List[int]) -> int:
#         if not height:
#             return 0

#         length = len(height)

#         # 初始化动态数组
#         # maxleft[i] 表示下标 i 左边最高柱子的高度
#         # maxright[j] 表示下标 j 右边最高柱子的高度
#         max_left = [0] * length
#         max_right = [0] * length
#         max_left[0] = height[0]
#         max_right[length - 1] = height[length - 1]
#         # 从左到右获取 maxleft
#         for i in range(1, length):
#             max_left[i] = max(height[i], max_left[i - 1])
#         # 从右到左获取 max_right
#         for j in range(length - 2, -1, -1):
#             max_right[j] = max(height[j], max_right[j + 1])

#         result = 0
#         # 依次遍历每个下标，之前已经获取到该下标左边和右边的最大值
#         # 取两者最小的，再减去当前位置实际的值，就是当前位置可以接到的雨水
#         # 因为之前生成 max_left 和 max_right 数组时，已经和当前位置实际的值比较取最大值
#         # 所以两者的最小值一定不小于当前位置实际的值
#         for idx in range(0, length):
#             result = result + (min(max_left[idx], max_right[idx]) - height[idx])

#         return result

# @lc code=end

