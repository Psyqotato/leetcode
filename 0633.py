class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0: return True
        while c != 1 and c % 2 == 0:
            c = c // 2
        if c % 4 == 3: return False
        start = int(sqrt(c))
        for i in range(3, start+1, 4):
            if c % i == 0:
                count = 0
                while c % i == 0:
                    count += 1
                    c //= i
                if count % 2 != 0:return False
            else:
                continue       
        return True