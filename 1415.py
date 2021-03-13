class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        import math

        if k > int(3 * math.pow(2, n-1)): return ""
        strs = ''
        if k > math.pow(2, n):
            strs = strs + 'c'
            k = k - math.pow(2, n)
        elif k > math.pow(2, n - 1):
            strs = strs + 'b'
            k = k - math.pow(2, n - 1)
        else: strs = strs + 'a'
        l = ['a','b','c']
        n = n - 1
        while n != 0:
            l.remove(strs[-1])
            if k > math.pow(2, n - 1):
                strs = strs + l[-1]
                k = k - math.pow(2, n - 1)
            else:
                strs = strs + l[0]
            l = ['a','b','c']
            n = n - 1
        return strs