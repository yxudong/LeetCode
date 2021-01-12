#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#

# @lc code=start

# Tips: array, greedy, binary-search

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 新建数组 sub_array，用于保存最长上升子序列
        # 对原序列进行遍历，将每位元素二分插入 sub_array 中
        # 1. 如果 sub_array 中元素都比它小，将它插到最后
        # 2. 否则，用它覆盖掉比它大的元素中最小的那个
        # 总之，思想就是让 sub_array 中存储比较小的元素
        # 这样，sub_array 未必是真实的最长上升子序列，但长度是对的
        if not nums:
            return 0

        sub_array = [nums[0]]
        len_sub_array = 1
        for i in range(1, len(nums)):
            if nums[i] > sub_array[-1]:
                # sub_array 中元素都比它小，将它插到最后
                sub_array.append(nums[i])
                len_sub_array = len_sub_array + 1
                continue
            # 二分插入 sub_array 中
            # 覆盖掉比它大的元素中最小的那个
            left, right = 0, len_sub_array - 1
            while left < right:
                mid = left + (right - left) // 2
                if sub_array[mid] < nums[i]:
                    left = mid + 1
                else:
                    # 注意这里是 right = mid，不是 right = mid - 1
                    # 因为要寻找比它大的元素中最小的那个
                    right = mid
            sub_array[left] = nums[i]

        return len_sub_array

# Tips: array, dynamic-programming

# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         # 定义 dp[i] 为考虑前 i 个元素，以第 i 个数字结尾的最长上升子序列的长度
#         # 注意 nums[i] 必须被选取
#         # 求解 dp[i] 时，向前遍历找出比 i 元素小的元素 j，令 dp[i] 为 dp[i], dp[j]+1)
#         length = len(nums)
#         dp = [1] * length
#         for i in range(length):
#             for j in range(i):
#                 # 只有 nums[j] < nums[i]，才更新数组
#                 # 因为需要严格上升，所以是 <，不是 <=
#                 if nums[j] < nums[i]:
#                     dp[i] = max(dp[i], dp[j] + 1)

#         # 注意这里不是 dp[-1]，因为最长子序列不一定是以数组最后一个元素结尾，要取数组中最大的
#         return max(dp)

# @lc code=end

