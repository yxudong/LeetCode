#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start

#Tips: array, stack

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # 采用单调栈，栈中记录数组下标，栈中数组下标对应的值从栈底到栈顶是递减的
        stack = []
        length = len(T)
        # 初始化数组全部为 0
        ans_list = [0] * length
        for i in range(0, length):
            # 为了计算下标的差值，所以栈中记录的是下标，而不是实际的值
            # while 循环直到栈为空，或者当前下标对应的值比栈顶下标对应的值小为止
            while stack and T[i] > T[stack[-1]]:
                # 如果栈中有元素并且当前下标对应的值比栈顶下标对应的值大
                # 说明遇到了下一个大的值，弹出元素
                idx = stack.pop()
                # 更新结果数组对应的下标的值
                ans_list[idx] = i - idx
            # 此时只可能栈为空，或者当前下标对应的值比栈顶下标对应的值小
            # 无论是哪种情况，都把当前下标加入栈中
            stack.append(i)

        return ans_list

# @lc code=end

