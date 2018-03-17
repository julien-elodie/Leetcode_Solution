class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n = n
        self.board = [0] * self.n
        self.boards = []
        self.trail()
        return self.printBoard()

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
            self.boards.append(self.board[:])
        for row in range(self.n):
            if self.place([col, row]):
                self.board[col] = row
                self.trail(col + 1)

    def printBoard(self):
        rets = []
        for board in self.boards:
            ret = []
            for row in range(self.n):
                rows = ["."] * self.n
                rows[board[row]] = "Q"
                ret.append("".join(rows))
            rets.append(ret)
        return rets


if __name__ == "__main__":
    s = Solution()
    output = s.solveNQueens(4)
    print(output)