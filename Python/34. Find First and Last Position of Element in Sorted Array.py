"""Solution for problem #34. Find First and Last Position of Element in Sorted Array

Description: Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?
"""

import unittest

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        found, result = False, [-1, -1]

        nums.append(-1)

        for i, v in enumerate(nums):
            if v == target and not found:
                result[0] = i
                found = True

            elif v != target and found:
                result[1] = i - 1
                break

        return result 

class UnitTestsForSolution(unittest.TestCase):
    def test_no_1(self):
        nums = [5,7,7,8,8,10]
        target = 8

        output = [3, 4]

        solution = Solution()
        self.assertEqual(output, solution.searchRange(nums, target))

    def test_no_2(self):
        nums = [5,7,7,8,8,10]
        target = 6

        output = [-1, -1]

        solution = Solution()
        self.assertEqual(output, solution.searchRange(nums, target))

    def test_no_3(self):
        nums = []
        target = 0

        output = [-1, -1]

        solution = Solution()
        self.assertEqual(output, solution.searchRange(nums, target))

    def test_no_4(self):
        nums = [1]
        target = 1

        output = [0, 0]

        solution = Solution()
        self.assertEqual(output, solution.searchRange(nums, target))

    def test_no_5(self):
        nums = [2, 2]
        target = 2

        output = [0, 1]

        solution = Solution()
        self.assertEqual(output, solution.searchRange(nums, target))        

if __name__ == '__main__':
    unittest.main()