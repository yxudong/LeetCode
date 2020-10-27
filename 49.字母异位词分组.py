#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start

# Tips: string, hash-table

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = {}
        for each_str in strs:
            sorted_str = "".join(sorted(each_str))
            if str_map.get(sorted_str, None) is None:
                str_map[sorted_str] = [each_str]
            else:
                str_map[sorted_str].append(each_str)

        ans_list = []
        for each in str_map.values():
            ans_list.append(each)

        return ans_list

# @lc code=end

