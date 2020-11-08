#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start

#Tips: array

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        result = nums[0]
        for i in range(1, len(nums)):
            if result == nums[i]:
                count = count + 1
            else:
                if count == 0:
                    result = nums[i]
                    count = 1
                else:
                    count = count - 1

        return result

# @lc code=end

