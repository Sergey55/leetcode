"""Solutio for propblem #35. Search Insert Position

Description: Given a sorted array of distinct integers and a target value, return the index
if the target is found. If not, return the index where it would be if it were inserted in order.
"""

import unittest

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        for i, v in enumerate(nums):
            if v == target or v > target:
                return i

        return len(nums)

        # l, r = 0, len(nums) - 1

        # while l < r:
        #     mid = int((l + r) / 2)

        #     print(l, mid, r)

        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] > target:
        #         r = mid
        #     else:
        #         l = mid

        # mid = int((l + r) / 2)

        # return (mid - 1) if nums[mid] > target else mid + 1 

class UnitTestsForSolution(unittest.TestCase):
    def test_no_1(self):
        nums = [1,3,5,6]
        target = 5

        output = 2

        solution = Solution()
        self.assertEqual(output, solution.searchInsert(nums, target))

    def test_no_2(self):
        nums = [1,3,5,6]
        target = 2

        output = 1

        solution = Solution()
        self.assertEqual(output, solution.searchInsert(nums, target))

    def test_no_3(self):
        nums = [1,3,5,6]
        target = 7

        output = 4

        solution = Solution()
        self.assertEqual(output, solution.searchInsert(nums, target))

    def test_no_4(self):
        nums = [1,3,5,6]
        target = 0

        output = 0

        solution = Solution()
        self.assertEqual(output, solution.searchInsert(nums, target)) 

    def test_no_5(self):
        nums = [1]
        target = 0

        output = 0

        solution = Solution()
        self.assertEqual(output, solution.searchInsert(nums, target))         

if __name__ == '__main__':
    unittest.main()