# Solution for problem `ZigZag Conversion`
#
# Description: The string "PAYPALISHIRING" is written in a 
# zigzag pattern on a given number of rows like this: (you 
# may want to display this pattern in a fixed font for better 
# legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);
#
# Ex 1:
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
import unittest

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s
        
        result = [''] * numRows
        
        const = numRows + (numRows - 2)
        
        for i, c in enumerate(s):
            row = i % const
            
            if row >= numRows:
                row = const - row
                
            result[row] += c
            
        return ''.join(result)

class TestsForSolution(unittest.TestCase):

    def test_PAYPALISHIRING_string(self):
        inputString = "PAYPALISHIRING"
        numRows = 3

        output = "PAHNAPLSIIGYIR"

        solution = Solution()

        self.assertEqual(output, solution.convert(inputString, numRows))

    def test_one_character_string(self):
        inputString = "A"
        numRows = 3

        output = "A"

        solution = Solution()

        self.assertEqual(output, solution.convert(inputString, numRows))        

if __name__ == '__main__':
    unittest.main()