#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start

# Tips: array, sort

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # 每个区间按第一个数字排序
        intervals.sort(key=lambda each: each[0])
        ans_list = []
        tmp_interval = intervals[0]
        for each_interval in intervals:
            if each_interval[0] <= tmp_interval[1]:
                # 如果当前区间的第一个数比 tmp_interval 最后一个小或等于，必然重合
                tmp_interval[1] = max(each_interval[1], tmp_interval[1])
            else:
                ans_list.append(tmp_interval)
                tmp_interval = each_interval

        # 循环过后最后一个 tmp_interval 不会被处理，所以这里加上
        ans_list.append(tmp_interval)

        return ans_list

# @lc code=end

