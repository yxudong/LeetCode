#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start

# Tips: hash-table

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, each_num in enumerate(nums):
            if target - each_num in hashtable:
                return [hashtable[target - each_num], i]
            hashtable[each_num] = i

        return []

# @lc code=end

