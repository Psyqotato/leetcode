class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lenth = len(s)
        if lenth == 0: return 0
        num, i = 1, 0
        while lenth - i >= num:
            for j in range(i+num,lenth+1):
                m = len(set(s[i:j]))
                num = max(m,num)
                if (m < (j - i)):break
            i = i + 1
        return num