class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j != 0:
                    grid[i][j] += grid[i][j - 1]
                elif i != 0 and j == 0:
                    grid[i][j] += grid[i - 1][j]
                elif i != 0 and j != 0:
                    grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])
        return grid[m - 1][n - 1]


if __name__ == "__main__":
    s = Solution()
    output = s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
    print(output)