"""Solution for problem #38. Count and Say

Description: The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

    countAndSay(1) = "1"
    countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.

To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character. Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

For example, the saying and conversion for digit string "3322251":

Given a positive integer n, return the nth term of the count-and-say sequence.
"""

import unittest

class Solution:
    def countAndSay(self, n: int) -> str:
        if n > 1:
            countAndSayPrev = self.countAndSay(n - 1)

            prevCharacter = countAndSayPrev[0]
            cnt = 0

            res = ''

            for c in countAndSayPrev:
                if c == prevCharacter:
                    cnt += 1
                else:
                    res += str(cnt)
                    res += prevCharacter

                    cnt = 1
                    prevCharacter = c
            
            res += str(cnt)
            res += prevCharacter

            return res
        else:
            return "1"



class TestsForSolution(unittest.TestCase):
    def test_no_1(self):
        n = 1
        output = "1"

        solution = Solution()
        self.assertEqual(output, solution.countAndSay(n))

    def test_no_2(self):
        n = 4
        output = "1211"

        solution = Solution()
        self.assertEqual(output, solution.countAndSay(n))

    def test_no_3(self):
        n = 3
        output = "21"

        solution = Solution()
        self.assertEqual(output, solution.countAndSay(n))        

if __name__ == '__main__':
    unittest.main()