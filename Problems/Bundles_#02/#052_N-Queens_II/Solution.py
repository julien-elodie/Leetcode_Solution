class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.n = n
        self.board = [0] * self.n
        self.count = 0
        return self.trail()

    def place(self, position):
        """
        :type position: List[int]
        :rtype: bool
        """
        col, row = position
        for index in range(col):
            if row == self.board[index] or abs(col - index) == abs(
                    row - self.board[index]):
                return False
        return True

    def trail(self, col=0):
        if col == self.n:
            self.count += 1
        for row in range(self.n):
            if self.place([col, row]):
                self.board[col] = row
                self.trail(col + 1)
        return self.count


if __name__ == "__main__":
    s = Solution()
    output = s.totalNQueens(4)
    print(output)