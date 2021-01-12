#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start

# Tips: array

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 把数组中的元素与索引建立一一对应的关系
        # 因为索引是确定的 0 到 n-1，一个也不缺，而数组的元素不确定，少了哪个也不知道
        # 既然两者是一一对应的关系，那么对数组中的每个元素对应的索引做个标记
        # 然后再对索引进行一次遍历，那么不存在的元素就不会有相应的标记，由此可查找出这些不存在的元素

        # 具体方法：
        #     将所有正数作为数组下标，置对应数组值为负值（相当于做一个标记）
        #     那么，仍为正数的位置即为（未出现过）消失的数字
        # 例如：
        #     原始数组：[4,3,2,7,8,2,3,1]
        #     重置后为：[-4,-3,-2,-7,8,2,-3,-1]
        #     结论：[8,2] 分别对应的 index 为 [5,6]（消失的数字）
        for num in nums:
            # 这里需要取绝对值，因为虽然原数组全部元素都是正数，但是遍历的过程中可能把元素设为负数
            num = abs(num)
            # 这里需要的数组下标需要 num - 1，防止数组越界
            # 又取一遍绝对值原因同上面取绝对值
            nums[num - 1] = abs(nums[num - 1]) * -1
        ans_list = []
        for i in range(len(nums)):
            # 再次遍历，遇到 > 0（相当于没做过标记）的就是没有出现过的元素
            if nums[i] > 0:
                # 因为之前是 - 1 做标记，这里注意最终结果 + 1
                ans_list.append(i + 1)

        return ans_list

# @lc code=end

