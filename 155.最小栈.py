#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start

# Tips: stack

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_data = None

    def push(self, x: int) -> None:
        if not self.stack:
            # 如果 stack 中没有元素，差值为 0，加入栈
            self.stack.append(0)
            self.min_data = x
        else:
            # 计算要 push 的元素和最小值的差值
            diff = x - self.min_data
            self.stack.append(diff)
            if diff < 0:
                # 如果差值小于 0，说明比最小值小，更新最小值
                self.min_data = x
        return

    def pop(self) -> None:
        # 获取到栈顶元素，并把栈顶元素弹出，这是一个差值
        diff = self.stack.pop()
        if diff < 0:
            # 如果弹出的栈顶元素小于 0，说明弹出的元素是最小值
            # 弹出的元素代表和上一个最小值的差值，所以更新最小值，min_data = min_data - diff
            self.min_data = self.min_data - diff
        return

    def top(self) -> int:
        if self.stack[-1] > 0:
            # 如果栈顶元素 > 0，说明该元素比最小值大
            # 因为栈中存的是和最小值的差值，所以加上最小值返回
            return self.min_data + self.stack[-1]
        else:
            # 如果栈顶元素 < 0，说明该元素比之前的最小值小
            # self.min_data 已经是栈顶元素
            return self.min_data

    def getMin(self) -> int:
        return self.min_data

# Tips: stack

# class MinStack:
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []
#         # 辅助栈
#         self.min_stack = []

#     def push(self, x: int) -> None:
#         self.stack.append(x)
#         if self.min_stack:
#             # 如果 push 的元素比辅助栈的 top 小
#             if x <= self.min_stack[-1]:
#                 # 注意这里的判断一定要用 <=，否则 pop 的时候判断相等就把辅助栈的元素弹出
#                 # 如果有两个相等的最小值，会导致错误
#                 self.min_stack.append(x)
#         else:
#             self.min_stack.append(x)
#         return

#     def pop(self) -> None:
#         pop_data = self.stack.pop()
#         if pop_data == self.min_stack[-1]:
#             # 如果 pop 的元素和辅助栈的 top 相等
#             self.min_stack.pop()
#         return

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

