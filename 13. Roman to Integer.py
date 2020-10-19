"""Solution for problem #13 `Roman to Integer`

Description: Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer."""

import unittest

class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0

        symbols = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        previous = s[0]
        result += symbols[previous]

        for c in s[1:]:
            if symbols[c] <= symbols[previous]:
                result += symbols[c]
            else:
                result += (symbols[c] - symbols[previous] - symbols[previous])

            previous = c

        return result

class TestsForSolution(unittest.TestCase):

    def test_no_1(self):
        input = 'III'
        output = 3

        solution = Solution()
        self.assertEqual(output, solution.romanToInt(input))

    def test_no_2(self):
        input = 'IV'
        output = 4

        solution = Solution()
        self.assertEqual(output, solution.romanToInt(input))

    def test_no_3(self):
        input = 'LVIII'
        output = 58

        solution = Solution()
        self.assertEqual(output, solution.romanToInt(input))

    def test_no_4(self):
        input = 'IX'
        output = 9

        solution = Solution()
        self.assertEqual(output, solution.romanToInt(input))

    def test_no_5(self):
        input = 'MCMXCIV'
        output = 1994

    #     solution = Solution()
    #     self.assertEqual(output, solution.romanToInt(input))        

if __name__ == '__main__':
    unittest.main()
        