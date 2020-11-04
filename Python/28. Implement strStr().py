""" Soltion for problem #28. Implement strStr()

Description: Return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question 
to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. 
This is consistent to C's strstr() and Java's indexOf().
"""

import unittest

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        l = len(needle)
            
        for i in range(len(haystack) - l + 1):
            if haystack[i: i + l] == needle:
                return i

        return -1

class TestsForSolution(unittest.TestCase):
    def test_no_1(self):
        heystack = "hello"
        needle = "ll"
        output = 2

        solution = Solution()
        self.assertEqual(output, solution.strStr(haystack=heystack, needle=needle))

    def test_no_2(self):
        heystack = "aaaaa"
        needle = "baa"
        output = -1

        solution = Solution()
        self.assertEqual(output, solution.strStr(haystack=heystack, needle=needle))

    def test_no_3(self):
        heystack = ""
        needle = ""
        output = 0

        solution = Solution()
        self.assertEqual(output, solution.strStr(haystack=heystack, needle=needle))

if __name__ == '__main__':
    unittest.main()