#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start

#Tips: bit-manipulation, dynamic-programming

class Solution:
    def countBits(self, num: int) -> List[int]:
        ans_list = [0] * (num + 1)
        for i in range(1, num + 1):
            # 先判断这个数是奇数还是偶数
            if i % 2 != 0:
                # 如果这个数是奇数：
                # 二进制表示中，奇数一定比前面那个偶数多一个 1
                # 因为多的就是最低位的 1
                ans_list[i] = ans_list[i - 1] + 1
            else:
                # 如果这个数是偶数：
                # 二进制表示中，偶数中 1 的个数一定和除以 2 之后的那个数一样多
                # 因为最低位是 0，除以 2 就是右移一位，也就是把那个 0 抹掉而已，
                # 所以 1 的个数是不变的
                ans_list[i] = ans_list[int(i / 2)]

        return ans_list

# @lc code=end

