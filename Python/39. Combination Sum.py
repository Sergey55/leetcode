""" Solution for problem #39. Combination Sum

Description: Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input."""

import unittest

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        result = []

        def f(arr, needed):
            if needed == 0:
                result.append(arr)
                return
            else:
                for v in candidates:
                    if v <= needed and ((not arr) or (arr and v >= arr[-1])):
                        f(arr + [v], needed - v)

        f([], target)
        return result

class TestsForSolution(unittest.TestCase):
    def test_no_1(self):
        candidates = [2,3,6,7]
        target = 7

        output = [[2,2,3],[7]]

        solution = Solution()
        self.assertEqual(output, solution.combinationSum(candidates, target))

    def test_no_2(self):
        candidates = [2,3,5]
        target = 8

        output = [[2,2,2,2],[2,3,3],[3,5]]

        solution = Solution()
        self.assertEqual(output, solution.combinationSum(candidates, target))

    def test_no_3(self):
        candidates = [2]
        target = 1

        output = []

        solution = Solution()
        self.assertEqual(output, solution.combinationSum(candidates, target))

    def test_no_4(self):
        candidates = [1]
        target = 1

        output = [[1]]

        solution = Solution()
        self.assertEqual(output, solution.combinationSum(candidates, target))

    def test_no_5(self):
        candidates = [1]
        target = 2

        output = [[1, 1]]

        solution = Solution()
        self.assertEqual(output, solution.combinationSum(candidates, target))

if __name__ == '__main__':
    unittest.main()