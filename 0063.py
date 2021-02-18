class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int: 
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0] == 1:return 0
        obstacleGrid[0][0] = -1
        for j in range(1,n):
            if obstacleGrid[0][j] != 1:
                if obstacleGrid[0][j-1] == -1:obstacleGrid[0][j] = -1
                else:obstacleGrid[0][j] = 0
        for i in range(1,m):
            if obstacleGrid[i][0] != 1:
                if obstacleGrid[i-1][0] == -1:obstacleGrid[i][0] = -1
                else:obstacleGrid[i][0] = 0
        print(obstacleGrid)
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] != 1:
                    if obstacleGrid[i][j-1] != 1 and obstacleGrid[i-1][j] != 1:
                        obstacleGrid[i][j] = obstacleGrid[i][j-1] + obstacleGrid[i-1][j]
                    elif obstacleGrid[i][j-1] == 1 and obstacleGrid[i-1][j] == 1:
                        obstacleGrid[i][j] = 0
                    else:
                        obstacleGrid[i][j] = obstacleGrid[i][j-1] + obstacleGrid[i-1][j] - 1
        return (0 - obstacleGrid[m-1][n-1])