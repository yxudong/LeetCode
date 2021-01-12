#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start

# Tips: array

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 因为输出数组不算在空间复杂度内，可以将 left_product 或 right_product 数组用输出数组来计算
        # 先把输出数组当作 left_product 数组来计算，然后再动态构造 right_product 数组得到结果

        # 初始化 ans_product 数组，对于给定索引 i，ans_product[i] 代表的是 i 左侧所有数字的乘积
        # 构造方式和之前相同，只是试图节省空间，先把 ans_product 作为上一种方法的 left_product 数组
        length = len(nums)
        ans_product = [1] * length
        for i in range(1, length):
            ans_product[i] = nums[i - 1] * ans_product[i - 1]

        # 唯一变化就是没有构造 right_product 数组，而是用一个变量来跟踪右边元素的乘积
        # 并更新数组 ans_product[idx] = ans_product[idx] * right_product
        # 然后 right_product 更新为 right_product = right_product * nums[i]
        right_product = 1
        for idx in range(length - 1, -1, -1):
            ans_product[idx] = ans_product[idx] * right_product
            right_product = right_product * nums[idx]

        return ans_product

# Tips: array

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         # 对于给定索引 i，使用它左边所有数字的乘积乘以右边所有数字的乘积

#         # 初始化两个空数组 left_product 和 right_product
#         # 对于给定索引 i，left_product[i] 代表的是 i 左侧所有数字的乘积
#         # right_product[i] 代表的是 i 右侧所有数字的乘积

#         # 用两个循环来填充 left_product 和 right_product 数组的值
#         # 对于数组 left_product，left_product[0] 应该是 1，因为第一个元素的左边没有元素
#         # 对于其他元素：left_product，left_product[i] = left_product[i-1] * nums[i-1]
#         length = len(nums)
#         left_product = [1] * length
#         for i in range(1, length):
#             left_product[i] = nums[i - 1] * left_product[i - 1]

#         # right_product 同理
#         right_product = [1] * length
#         for j in range(length - 2, -1, -1):
#             right_product[j] = nums[j + 1] * right_product[j + 1]

#         # 最后在输入数组上迭代，索引 idx 处的值为：left_product[idx] * right_product[idx]
#         ans = [0] * length
#         for idx in range(0, length):
#             ans[idx] = left_product[idx] * right_product[idx]

#         return ans

# @lc code=end

