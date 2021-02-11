class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:return s
        strings = ''
        for k in range(numRows):
            num, switch = k, 1
            while num < len(s):
                strings = strings + s[num]
                if (k == 0) or (k == numRows - 1):num = num + (numRows-1)*2
                elif switch > 0 :num = num + ((numRows-1)*2 - k*2)
                else:num = num + k*2
                switch = 0 - switch
        return strings