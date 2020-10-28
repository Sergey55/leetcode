"""Solutio for problem #22 `Generate Parentheses`

Description: Given n pairs of parentheses, write a function 
to generate all combinations of well-formed parentheses.
"""

import unittest

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        cache = {
            1: ['()']
        }

        def generate(n: int):
            if n == 0:
                return []

            if n in cache:
                return cache[n]
            else:
                result = []

                for i in range(n, 0, -1):
                    print(f'i: {i}')

                    if n - i == 0:
                        result.extend(['(' + v + ')' for v in generate(n - 1) ])
                    else:
                        result.extend([r1 + r2 for r1 in generate(i) for r2 in generate(n - i)])

                cache[n] = result

                return result

        result = generate(n)

        return list(set(result))


class TestsForSolution(unittest.TestCase):
    def test_no_1(self):
        n = 3
        output = ["((()))","(()())","(())()","()(())","()()()"]

        solution = Solution()
        self.assertEqual(set(output), set(solution.generateParenthesis(n)))

    def test_no_2(self):
        n = 1
        output = ["()"]

        solution = Solution()
        self.assertEqual(set(output), set(solution.generateParenthesis(n)))

    def test_no_3(self):
        n = 2
        output = ["(())", "()()"]

        solution = Solution()
        self.assertEqual(set(output), set(solution.generateParenthesis(n)))

    def test_no_4(self):
        n = 4
        output = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]

        solution = Solution()
        self.assertEqual(set(output), set(solution.generateParenthesis(n)))

if __name__ == '__main__':
    unittest.main()