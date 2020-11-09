""" Solution for problem #31. Next Permutation

Description: Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.
"""

import unittest

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pass

class TestsForSolution(unittest.TestCase):
    def test_no_1(self):
        nums = [1, 2, 3]
        output = [1, 3, 2]

        solution = Solution()
        self.assertEqual(output, solution.nextPermutation(nums))

    def test_no_2(self):
        nums = [3,2,1]
        output = [1, 2, 3]

        solution = Solution()
        self.assertEqual(output, solution.nextPermutation(nums))

    def test_no_3(self):
        nums = [1,1,5]
        output = [1,5,1]

        solution = Solution()
        self.assertEqual(output, solution.nextPermutation(nums))

    def test_no_4(self):
        nums = [1]
        output = [1]

        solution = Solution()
        self.assertEqual(output, solution.nextPermutation(nums))          

if __name__ == "__main__":
    unittest.main()