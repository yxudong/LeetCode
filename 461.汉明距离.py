#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#

# @lc code=start

#Tips: bit-manipulation

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # 先对两个数取异或，得到的就是两个数字对应二进制位不同组成的数字
        # 例如：1 ^ 4 = 5
        # 1: 0 0 0 0 1
        # 4: 0 0 1 0 0
        # 5: 0 0 1 0 1
        xor = x ^ y
        count = 0
        while xor:
            # 一个数 & 1 可以判断对应二进制的最后一位是否为 1
            if xor & 1:
                count = count + 1
            # 每次向右移动一位
            xor = xor >> 1

        return count

# @lc code=end

