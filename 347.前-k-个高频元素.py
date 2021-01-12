#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start

# Tips: array, hash-table, heap

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 调整堆的函数
        def adjust_heap(array, start_pos, end_pos):
            temp = array[start_pos]
            pos = start_pos
            child_pos = pos * 2 + 1
            while child_pos <= end_pos:
                right_pos = child_pos + 1
                if right_pos <= end_pos and array[right_pos][1] > array[child_pos][1]:
                    child_pos = right_pos
                if temp[1] < array[child_pos][1]:
                    array[pos] = array[child_pos]
                    pos = child_pos
                    child_pos = 2 * pos + 1
                else:
                    break
            array[pos] = temp

        # 计数变成哈希表
        count_map = {}
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1

        # 把哈希表转成数组方便排序
        count_list = [(k, v) for k, v in count_map.items()]

        # 建立大根堆
        length = len(count_list)
        for i in range(length // 2, -1, -1):
            adjust_heap(count_list, i, length - 1)

        # 调整堆，每次选出一个最大的，循环 k 次
        ans = []
        for i in range(length - 1, length - 1 - k, -1):
            count_list[0], count_list[i] = count_list[i], count_list[0]
            adjust_heap(count_list, 0, i - 1)
            ans.append(count_list[i][0])

        return ans

# @lc code=end

