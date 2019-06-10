class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_1=[0]+digits
        l = len(digits_1) - 1
        for index,i in enumerate(digits_1):
            if digits_1[l-index] < 9:
                digits_1[l-index] +=1
                break
            else:
                digits_1[l-index] = 0
        if digits_1[0] == 1:
            return digits_1
        else:
            return digits_1[1:]
