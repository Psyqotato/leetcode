class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == '':return s
        result = s[0]
        s2 = list(set(s))
        lenth1 = len(s2)
        work = [[] for i in range(lenth1)]
        for i in range(len(s)):work[s2.index(s[i])].append(i)
        for i in range(lenth1):
            lenth2 = len(work[i])
            if (lenth2 <= 1):continue
            for x in range(lenth2-1):
                x1, num = work[i][x], len(result)
                if (work[i][-1] - x1) < num:break
                for y in range(lenth2-1,x,-1):
                    y1 = work[i][y]
                    if (y1 - x1 + 1) <= num:break
                    k = int((y1 -x1)/2)
                    if (y1 - x1) % 2 == 0:
                        if s[x1:x1+k] == s[x1+k+1:y1+1][::-1]:
                            result = s[x1:y1+1]
                            break
                    elif s[x1:x1+k+1] == s[x1+k+1:y1+1][::-1]:
                        result = s[x1:y1+1]
                        break
        return result