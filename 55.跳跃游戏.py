#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start

# Tips: array, greedy

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 代表从当前 0 开始可以走的最远距离
        far = 0
        length = len(nums)
        for i in range(0, length):
            if i > far:
                # 如果当前位置比最远可以走的距离远，返回 False
                return False
            if i + nums[i] > far:
                # 更新可以走的最远距离
                far = i + nums[i]

        return True

# @lc code=end

