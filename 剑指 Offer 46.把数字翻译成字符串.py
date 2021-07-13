# Tips: recursive, dynamic-programming

class Solution:
    def translateNum(self, num: int) -> int:
        input_str = str(num)
        length = len(input_str)
        if length <= 1:
            return length
        dp = [0 for _ in range(length)]
        dp[0] = 1
        if 9 < int(input_str[:2]) <= 25:
            dp[1] = 2
        else:
            dp[1] = 1

        for i in range(2, length):
            if 9 < int(input_str[i-1:i+1]) <= 25:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]

        return dp[-1]
