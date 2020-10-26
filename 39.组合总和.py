#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start

# Tips: backtracking

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def back(idx, tmp_sum, path):
            if tmp_sum == target:
                # 因为 path 会在每次都被修改，所以这里使用浅复制
                ans_list.append(path[:])
            if tmp_sum > target:
                return

            for i in range(idx, length):
                path.append(candidates[i])
                tmp_sum = tmp_sum + candidates[i]
                back(i, tmp_sum, path)
                tmp_sum = tmp_sum - candidates[i]
                path.pop()

        length = len(candidates)
        ans_list = []
        back(0, 0, [])
        return ans_list

# @lc code=end

