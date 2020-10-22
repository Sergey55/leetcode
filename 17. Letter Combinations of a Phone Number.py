"""Solution for problem #17 `Letter Combinations of a Phone Number`

Description: Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could 
represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) 
is given below. Note that 1 does not map to any letters."""

import unittest

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []

        lookup = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p','q','r','s'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']            
        }

        digits = int(digits)

        res = []
        
        while digits:
            div, mod = divmod(digits, 10)            

            res = self.product(lookup[mod], res)

            digits = div

        return [''.join(v) for v in res]
            
    def product(self, l, r):
        if not r:
            return l
        
        return [a + b for a in l for b in r]

class TestsForSolution(unittest.TestCase):
    def test_no_1(self):
        input = "23"
        output = ["ad","ae","af","bd","be","bf","cd","ce","cf"]

        solution = Solution()
        self.assertEqual(output, solution.letterCombinations(input))

    def test_no_2(self):
        input = ""
        output = []

        solution = Solution()
        self.assertEqual(output, solution.letterCombinations(input))

    def test_no_3(self):
        input = "2"
        output = ["a","b","c"]

        solution = Solution()
        self.assertEqual(output, solution.letterCombinations(input))

    def test_no_4(self):
        input = "9"
        output = ["w","x","y","z"]

        solution = Solution()
        self.assertEqual(output, solution.letterCombinations(input))

    def test_no_5(self):
        input = "234"
        output =  ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', 'afh', 'afi', 'bdg', 'bdh', 'bdi', 'beg', 'beh', 'bei', 'bfg', 'bfh', 'bfi', 'cdg', 'cdh', 'cdi', 'ceg', 'ceh', 'cei', 'cfg', 'cfh', 'cfi']

        solution = Solution()
        self.assertEqual(output, solution.letterCombinations(input))         

if __name__ == '__main__':
    unittest.main()