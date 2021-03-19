class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def combine1(num, kd):
            solutions = []
            for i in range(num, n - kd + 2):
                if kd == 1:
                    solutions.append([i])
                else: 
                    for j in combine1(i + 1, kd - 1):
                        solutions.append([i] + j)                
            return solutions
        return combine1(1, k)