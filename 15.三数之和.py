#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start

# Tips: sort, two-pointers

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lens = len(nums)
        if lens < 3:
            return []
        nums.sort()
        ans_list = []
        for i in range(lens):
            if nums[i] > 0:
                return ans_list
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = lens - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    ans_list.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[right] == nums[right - 1]:
                        right = right - 1
                    while left < right and nums[left] == nums[left + 1]:
                        left = left + 1
                    right = right - 1
                    left = left + 1
                else:
                    if nums[i] + nums[left] + nums[right] > 0:
                        right = right - 1
                    else:
                        left = left + 1

        return ans_list

# @lc code=end

