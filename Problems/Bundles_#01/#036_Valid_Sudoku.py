class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def isValid(line):
            ret = [i for i in line if i != '.']
            return len(ret) == len(set(ret))
        
        def isValid_Col(board):
            for col in board:
                if not isValid(col):
                    return False
            return True

        def isValid_Row(board):
            for row in zip(*board):
                if not isValid(row):
                    return False
            return True

        def isValid_Square(board):
            for i in (0, 3, 6):
                for j in (0, 3, 6):
                    square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                    if not isValid(square):
                        return False
            return True

        return isValid_Col(board) and isValid_Row(board) and isValid_Square(board)
                

if __name__ == "__main__":
    s = Solution()
    output = s.isValidSudoku(
        [
            [".", "8", "7", "6", "5", "4", "3", "2", "1"],
            ["2", ".", ".", ".", ".", ".", ".", ".", "."],
            ["3", ".", ".", ".", ".", ".", ".", ".", "."],
            ["4", ".", ".", ".", ".", ".", ".", ".", "."],
            ["5", ".", ".", ".", ".", ".", ".", ".", "."],
            ["6", ".", ".", ".", ".", ".", ".", ".", "."],
            ["7", ".", ".", ".", ".", ".", ".", ".", "."],
            ["8", ".", ".", ".", ".", ".", ".", ".", "."],
            ["9", ".", ".", ".", ".", ".", ".", ".", "."]
        ]
    )
    print(output)