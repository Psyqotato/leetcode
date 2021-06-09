class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:return s
        nn = (numRows - 1) * 2
        work = [""] * numRows
        for i in range(len(s)):
            if i % nn > nn / 2: switch = nn - i % nn
            else:
                switch = i % nn
            work[switch] = work[switch] + s[i]
        string = ""
        for i in range(numRows):
            string = string + work[i]
        return string