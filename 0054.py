class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        import numpy as np
        solutions = []
        solutions = solutions + matrix[0]
        matrix.remove(matrix[0])
        while matrix != []:
            a = np.rot90(matrix, 1)
            matrix = a.tolist()
            solutions = solutions + matrix[0]
            matrix.remove(matrix[0])
        return solutions