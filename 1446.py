class Solution:
    def maxPower(self, s: str) -> int:
        count, result = 1, 1
        for i in range(1,len(s)):
            if s[i - 1] == s[i]:
                count += 1
                result = max(result, count)
            else:
                count = 1
        return result