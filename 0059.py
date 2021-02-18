class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1: return [[1]]
        solutions = [[0] * n for row in range(n)]
        nums, k = 0, n
        i, j = 0, -1
        while nums < n ** 2:
            for _ in range(k):
                j, nums = j + 1, nums + 1
                solutions[i][j] = nums
            for _ in range(k - 1):
                i, nums = i + 1, nums + 1
                solutions[i][j] = nums
            for _ in range(k - 1):
                j, nums = j - 1, nums + 1
                solutions[i][j] = nums 
            for _ in range(k - 2):
                i, nums = i - 1, nums + 1
                solutions[i][j] = nums
            k -= 2   
        return solutions