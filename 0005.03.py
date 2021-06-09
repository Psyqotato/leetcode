class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == '' or len(s) == 1:return s
        result = s[0]
        for i in range(1,len(s)):
            mid = int((len(result) - 1)/2)
            if i - mid > 0 and i + mid <= len(s) - 1:
                if s[i] == s[i - 1] and s[i - mid - 1:i] == s[i:i + mid + 1][::-1]:
                    left, right = i - mid - 1, i + mid
                    while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                        left, right = left - 1, right + 1
                    if right - left > len(result):
                        result = s[left+1:right]
                if s[i - mid:i] == s[i + 1:i + mid + 1][::-1]:
                    left, right = i - mid, i + mid
                    while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                        left, right = left - 1, right + 1
                    if right - left > len(result):
                        result = s[left+1:right]
        return result