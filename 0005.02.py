class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == '' or len(s) == 1:return s
        result = s[0]
        for i in range(1,len(s)):
            left, right = i - 1, i
            if s[i] == s[i - 1]:
                while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                    left, right = left - 1, right + 1
            if right - left > len(result):
                result = s[left+1:right]
            left, right = i, i
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                left, right = left - 1, right + 1
            if right - left > len(result):
                result = s[left+1:right]
        return result