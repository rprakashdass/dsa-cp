"""
Time Complexity: O(n * n!)
    - n for every safety check
    - n! for all possible combination
Space Complexity: O(n ^ 2)
    - n ^ 2 for storing the board
    - recursion stack depth to n
"""

class Solution:
    def isSafe(self, board, row, col):
        # check same row
        for r in range(0, row):
            if board[r][col] == 'Q':
                return False

        # check upper left diagonal
        for r, c in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
            if board[r][c] == 'Q':
                return False

        # check upper right diagonal
        for r, c in zip(range(row-1, -1, -1), range(col+1, self.n)):
            if board[r][c] == 'Q':
                return False
        return True

    def placeQueen(self, board, row):
        if row == self.n:
            lis = [''.join(row) for row in board]
            self.result.append(lis)
            return

        for col in range(0, self.n):
            if not self.isSafe(board, row, col):
                continue
            board[row][col] = 'Q'
            self.placeQueen(board, row+1)
            board[row][col] = '.'

    def solveNQueens(self, n: int):
        self.n = n
        self.result = []
        board = [ ['.' for j in range(n)] for i in range(n) ]
        self.placeQueen(board, 0)
        return self.result