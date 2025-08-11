"""
Time Complexity: O(n!)
    - O(1) for every safety check
    - n! for all possible combination
Space Complexity: O(n ^ 2)
    - n ^ 2 for storing the board
    - 3n complexity for safe check storage
    - n for recursive stack depth
"""

class Solution:
    def isSafe(self, row, col):
        if col in self.column:
            return False
        if row + col in self.posDiagonal:
            return False
        if row - col in self.negDiagonal:
            return False
        return True

    def placeQueen(self, board, row):
        if row == self.n:
            lis = [''.join(row) for row in board]
            self.result.append(lis)
            return

        for col in range(0, self.n):
            if not self.isSafe(row, col):
                continue
            self.column.add(col)
            self.posDiagonal.add(row + col)
            self.negDiagonal.add(row - col)

            board[row][col] = 'Q'
            self.placeQueen(board, row+1)
            board[row][col] = '.'

            self.column.remove(col)
            self.posDiagonal.remove(row + col)
            self.negDiagonal.remove(row - col)

    def solveNQueens(self, n: int):
        self.n = n
        self.result = []

        self.column = set()
        self.posDiagonal = set()
        self.negDiagonal = set()

        board = [ ['.' for j in range(n)] for i in range(n) ]
        self.placeQueen(board, 0)
        return self.result