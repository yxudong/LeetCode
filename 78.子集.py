#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start

# Tips: array, iteration

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 直接从前遍历，遇到一个数就把所有子集加上该数组成新的子集，遍历完毕即是所有子集
        if not nums:
            return []
        ans_list = []
        for i in nums:
            tmp = []
            for item in ans_list:
                # 遍历并加上新的数字
                copy_item = item[:]
                copy_item.append(i)
                tmp.append(copy_item)
            # 加上只有当前数字组成的列表
            tmp.append([i])
            ans_list.extend(tmp[:])
        # 空列表也算做子集，前面的循环没有加入
        ans_list.append([])

        return ans_list

# Tips: array, bit-manipulation

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         """
#         二进制
#         对应数字     1    2    3   对应子集
#         0           0    0    0    []
#         1           0    0    1    [3]
#         2           0    1    0    [2]
#         3           0    1    1    [2,3]
#         4           1    0    0    [1]
#         5           1    0    1    [1,3]
#         6           0    1    1    [2,3]
#         7           1    1    1    [1,2,3]
#         """
#         length = len(nums)
#         ans_list = []
#         # 最终结果的长度 total_len = 1 << length，此处位运算表示的是 2 ** n
#         total_len = 1 << length
#         for i in range(0, total_len):
#             tmp = []
#             for j in range(0, length):
#                 if i >> j & 1:
#                     # 条件 i >> j & 1，表示第 j 位是否为 1，若满足，则将该位元素加入中间结果 tmp 中
#                     tmp.append(nums[j])
#             ans_list.append(tmp)

#         return ans_list

# Tips: array, backtracking

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         def back(idx, path):
#             """
#             # print("idx: " + str(idx), " path: " + str(path))
#             # idx: 0  path: []
#             # idx: 1  path: [1]
#             # idx: 2  path: [1, 2]
#             # idx: 3  path: [1, 2, 3]
#             # idx: 3  path: [1, 3]
#             # idx: 2  path: [2]
#             # idx: 3  path: [2, 3]
#             # idx: 3  path: [3]
#             """
#             ans_list.append(path)
#             if idx == length:
#                 return
#             for i in range(idx, length):
#                 back(i + 1, path + [nums[i]])

#         ans_list = []
#         length = len(nums)
#         back(0, [])
#         return ans_list

# @lc code=end

