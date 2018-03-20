class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.factorial(m + n - 2) // self.factorial(
            m - 1) // self.factorial(n - 1)

    def factorial(self, n):
        ret = 1
        for i in range(1, n + 1):
            ret *= i
        return ret


if __name__ == "__main__":
    s = Solution()
    output = s.uniquePaths(1, 2)
    print(output)
