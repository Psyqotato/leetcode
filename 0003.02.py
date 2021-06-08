class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        max_num = 1
        nums = [i for i in range(len(s),0,-1)]
        for i in range(len(s)):
            if nums[i] < max_num:continue
            left, right = i, len(s) - 1
            while (left < right) and (max_num < right - i + 1):
                if s[left+1:right+1].find(s[left]) != -1:
                    right = s[left+1:right+1].find(s[left]) + left
                    nums[left] = right - left
                left += 1
            nums[i] = right - i + 1
            if nums[i] > max_num: max_num = nums[i]
        return max_num