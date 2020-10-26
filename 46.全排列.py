#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start

# Tips: backtracking

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def back(used, path):
            if len(path) == length:
                # 因为 path 会在每次都被修改，所以这里使用浅复制
                ans_list.append(path[:])
                return

            for i in range(length):
                if used[i] == 1:
                    continue
                used[i] = 1
                path.append(nums[i])
                back(used, path)
                path.pop()
                used[i] = 0
            pass

        length = len(nums)
        used = [0 for _ in range(length)]
        ans_list = []
        back(used, [])
        return ans_list

# @lc code=end

