class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def findqueen(lutions,n):
            solution = []
            nums = len(lutions)
            for i in range(0,n):
                if i not in lutions:
                    solution.append(i)
                    for j in range(0,nums):
                        if nums - j == i - lutions[j] or nums - j == lutions[j] - i:
                            solution.pop()
                            break
            solutions = []
            if nums < n - 1 and solution != []:
                for i in solution:
                    lutions.append(i)
                    for j in findqueen(lutions,n):solutions.append([i] + j)
                    else:lutions.pop()
            elif nums == n - 1:
                for i in solution:solutions.append([i])
            return solutions
        if n == 1:return [["Q"]]
        solutions = []
        printsolutions = []
        for i in range(0,n):
            for j in findqueen([i],n):solutions.append([i] + j)
        for i in range(0,len(solutions)):
            a = []
            for j in range(0,n):
                a.append("." * solutions[i][j] + "Q" + "." * (n - solutions[i][j] - 1))
            printsolutions.append(a)
        return printsolutions