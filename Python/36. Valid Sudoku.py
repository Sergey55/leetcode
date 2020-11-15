"""Solution for problem #36. Valid Sudoku

Description: Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

* Each row must contain the digits 1-9 without repetition.
* Each column must contain the digits 1-9 without repetition.
* Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

* A Sudoku board (partially filled) could be valid but is not necessarily solvable.
* Only the filled cells need to be validated according to the mentioned rules.
"""

import unittest

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check each row
        for row in range(len(board)):
            s = set()

            for v in board[row]:
                if v != '.':
                    if v not in s:
                        s.add(v)
                    else:
                        return False

        # Check each col
        for col in range(len(board[0])):
            s = set()

            for row in range(len(board)):
                if board[row][col] != '.':
                    if board[row][col] not in s:
                        s.add(board[row][col])
                    else:
                        return False

        # Check each 3 x 3 sub-box
        for row in range(0, len(board), 3):
            for col in range(0, len(board[0]), 3):

                s = set()

                for r in range(row, row + 3):
                    for c in range(col, col + 3):

                        if board[r][c] != '.':
                            if board[r][c] not in s:
                                s.add(board[r][c])
                            else:
                                return False                        

        return True

class TestForSolution(unittest.TestCase):
    def test_no_1(self):
        board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]

        output = True

        solution = Solution()
        self.assertEqual(output, solution.isValidSudoku(board))

    def test_no_2(self):
        board = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]

        output = False

        solution = Solution()
        self.assertEqual(output, solution.isValidSudoku(board))        

if __name__ == '__main__':
    unittest.main()