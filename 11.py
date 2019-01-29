class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area, i, j = 0, 0, len(height) - 1
        while i < j:
            if height[i] <= height[j]:
                less = height[i]
                i += 1
            else:
                less = height[j]
                j -= 1
            new = (j - i + 1) * less
            if new > area:
                area = new
        return area