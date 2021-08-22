class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        summ, minn, neg = 0, abs(matrix[0][0]), 0
        for i in matrix:
            for j in i:
                summ += abs(j)
                minn = min(minn, abs(j))
                if j < 0: neg += 1              
        return summ if neg % 2 == 0 else summ - minn * 2