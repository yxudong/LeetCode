class Solution:     
    def maxSubArray(self, nums):
        max_num, sum_num = nums[0], nums[0]
        for index, i in enumerate(nums):
            if index == 0:
                continue
            if sum_num < 0:
                sum_num = nums[index]
            else:
                sum_num += nums[index]
            if sum_num > max_num:
                max_num = sum_num

        return max_num
