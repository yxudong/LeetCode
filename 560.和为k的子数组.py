#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为K的子数组
#

# @lc code=start

# Tips: array, hash-table

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 采用哈希表记录前缀和
        pre_map = {}
        count = 0
        curr_sum  = 0
        for num in nums:
            curr_sum = curr_sum + num
            # 如果当前和正好等于 k，次数 + 1
            # 下面的两行必须要加，否则会漏掉当前和正好为 k 的情况
            # 或者可以把初始的哈希表设为 {0: 1}，而不是 {}
            if curr_sum == k:
                count = count + 1
            # 如果 curr_sum - k 在哈希表中存在，说明存在 前缀和 + k = curr_sum
            # 此时 [前缀和的位置 + 1, 当前位置] 正好是一个符合要求的子数组
            # 有多少个这样的前缀和，就有多少个这样的子数组，所以 + pre_map[curr_sum - k]
            if (curr_sum - k) in pre_map:
                count = count + pre_map[curr_sum - k]
            # 把当前的和存入哈希表
            if curr_sum in pre_map:
                pre_map[curr_sum] = pre_map[curr_sum] + 1
            else:
                pre_map[curr_sum] = 1

        return count

# @lc code=end

