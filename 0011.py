class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, s = 0, len(height) - 1, 0
        while (right - left) >= 1:
            s1 = min(height[left],height[right]) * (right - left)
            if s < s1: s = s1
            if height[left] > height[right]:right = right - 1
            elif height[right] >= height[left]:left = left + 1
        return s 