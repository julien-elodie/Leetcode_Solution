class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        ret = [[0] * (n + 1) for _ in range(m + 1)]
        ret[0][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if not obstacleGrid[i - 1][j - 1]:
                    ret[i][j] = ret[i - 1][j] + ret[i][j - 1]
        return ret[m][n]


if __name__ == "__main__":
    s = Solution()
    output = s.uniquePathsWithObstacles([[0]])
    print(output)
