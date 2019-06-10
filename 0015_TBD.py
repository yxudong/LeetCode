class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []

        res = []
        nums.sort()

        if nums[0] == nums[-1] == 0:                                    # special case, otherwise return [] for [0, 0, 0]
            return [[0, 0, 0]]

        for i in range(len(nums) - 2):                                  # iterate for the first number
            if nums[i] > 0:                                             # unnecessary to check if least number sis positive
                break
            if nums[i] == nums[i - 1]:                                  # avoiding duplication
                continue

            l, r = i + 1, len(nums) - 1                                 # rest 2 numbers start from far edges of afterward

            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:                                               # if neg, increase the smaller one
                    l += 1
                elif s > 0:                                             # if pos, decrease the greater one
                    r -= 1
                if s == 0:                                              # check, append and reduce duplication
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1                                              # see if other pairs check.
                    r -= 1
        return res