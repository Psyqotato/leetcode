class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lines = int(len(matrix)/2)
        lenth = len(matrix)
        for i in range(0,lines):
            lenth = lenth - 1
            for j in range(i,lenth):
                matrix[i][j], matrix[j][lenth] = matrix[j][lenth], matrix[i][j]
                matrix[i][j], matrix[lenth][lenth + i - j] = matrix[lenth][lenth + i - j], matrix[i][j]
                matrix[i][j], matrix[lenth + i - j][i] = matrix[lenth + i - j][i], matrix[i][j]