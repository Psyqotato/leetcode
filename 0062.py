class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        solutions = [[1] * n for row in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                solutions[i][j] = solutions[i][j-1] + solutions[i-1][j]
        return solutions[m-1][n-1]