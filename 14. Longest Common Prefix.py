"""Solution for problem #14 `Longest Common Prefix`

Description: Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string ""."""

import unittest

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ''

        minLength = min([len(s) for s in strs])

        for i in range(minLength):
            equal = True

            currentSymbol = strs[0][i]

            for str in strs[1:]:
                if str[i] != currentSymbol:
                    equal = False

            if not equal:
                return strs[0][:i]
            
        return strs[0][:minLength]

class TestsForSolution(unittest.TestCase):
    def test_no_1(self):
        input = ["flower","flow","flight"]
        output = 'fl'

        solution = Solution()
        self.assertEqual(output, solution.longestCommonPrefix(input))

    def test_no_2(self):
        input = ["dog","racecar","car"]
        output = ''

        solution = Solution()
        self.assertEqual(output, solution.longestCommonPrefix(input))

    def test_no_3(self):
        input = []
        output = ''

        solution = Solution()
        self.assertEqual(output, solution.longestCommonPrefix(input))             

if __name__ == '__main__':
    unittest.main()