class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index, i in enumerate(nums):
            if target < nums[0]:
                return 0
            if target == i:
                return index
            elif target > i and index < len(nums)-1 and target < nums[index+1]:
                return index + 1
            if index == len(nums)-1:
                return index + 1
