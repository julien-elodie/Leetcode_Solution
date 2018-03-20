class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[n * n]]
        while matrix[0][0] > 1:
            mapping = list(map(list, zip(*matrix[::-1])))
            ranging = [_ for _ in range(matrix[0][0] - len(matrix), matrix[0][0])]
            matrix = [ranging] + mapping
        return matrix * (n > 0)


if __name__ == "__main__":
    s = Solution()
    output= s.generateMatrix(3)
    print(output)