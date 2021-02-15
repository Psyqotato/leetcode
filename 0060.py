class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math
        strs = ""
        solutions = [x for x in range(1,n+1)]
        for i in range(0,n):
            for j in range(0,len(solutions)):
                if math.factorial(n-i-1) * (j+1) >= k:
                    strs = strs + str(solutions[j])
                    break
            k = k - math.factorial(n-i-1) * j
            solutions.remove(solutions[j])
        return strs