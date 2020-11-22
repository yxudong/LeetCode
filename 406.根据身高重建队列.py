#
# @lc app=leetcode.cn id=406 lang=python3
#
# [406] 根据身高重建队列
#

# @lc code=start

#Tips: array

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 首先按身高 h 降序排序，如果身高相等按 k 升序排序
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        # 例如：[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
        # 此时 [[7,0], [7,1], [6,1], [5,0], [5,2], [4,4]]
        ans_list = []
        for each in people:
            if len(ans_list) <= each[1]:
                # 如果当前结果数组长度小于等于 k，直接加入数组
                ans_list.append(each)
            else:
                # 如果当前结果数组长度大于 k，不能直接加入数组，需要加入到相应的位置
                ans_list.insert(each[1], each)

        return ans_list

# @lc code=end

