#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start

# Tips: string, backtracking

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return list()

        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        length = len(digits)

        def back(index):
            if index == length:
                ans_list.append("".join(tmp_list))
                return
            letters = phoneMap[digits[index]]
            for letter in letters:
                tmp_list.append(letter)
                back(index+1)
                tmp_list.pop()

        tmp_list = []
        ans_list = []
        back(0)

        return ans_list

# Tips: string, iteration

# class Solution:
    # def letterCombinations(self, digits: str) -> List[str]:
        # if not digits:
            # return list()

        # phoneMap = {
            # "2": "abc",
            # "3": "def",
            # "4": "ghi",
            # "5": "jkl",
            # "6": "mno",
            # "7": "pqrs",
            # "8": "tuv",
            # "9": "wxyz",
        # }

        # ans = []
        # for i, digit in enumerate(digits):
            # letters = phoneMap[digit]
            # if i == 0:
                # for letter in letters:
                    # ans.append(letter)
            # else:
                # tmp_list = []
                # for letter in letters:
                    # for each in ans:
                        # tmp_list.append(each + letter)
                # ans = tmp_list

        # return ans

# @lc code=end

