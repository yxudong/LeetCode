#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start

# Tips: backtracking

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def back(path):
            if len(path) == length:
                result.append(path[:])
                return

            for i in range(length):
                if is_used[i] == 0:
                    # 如果该位置的元素和前一个位置的元素相同（需要首先对数组排序）
                    # 并且前一个位置的元素已经使用过，就属于重复，不需要回溯
                    if i != 0 and nums[i] == nums[i-1] and is_used[i-1] == 1:
                        continue
                    is_used[i] = 1
                    back(path + [nums[i]])
                    is_used[i] = 0

            return

        nums.sort()
        length = len(nums)
        is_used = [0] * length
        result = []
        back([])
        return result

# @lc code=end

