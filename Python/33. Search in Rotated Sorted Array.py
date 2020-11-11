"""Solution for problem #33. Search in Rotated Sorted Array

Desciption: You are given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.
"""

import unittest

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = int((l + r) / 2)

            if nums[mid] == target:
                return mid

            if target >= nums[0]:
                if nums[mid] >= nums[0] and nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[mid] < nums[0] and nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1


class  TestsForSolution(unittest.TestCase):
    def test_no_1(self):
        nums = [4,5,6,7,0,1,2]
        target = 0
        output = 4

        solution = Solution()
        self.assertEqual(output, solution.search(nums, target))

    def test_no_2(self):
        nums = [4,5,6,7,0,1,2]
        target = 3
        output = -1

        solution = Solution()
        self.assertEqual(output, solution.search(nums, target))

    def test_no_3(self):
        nums = [1]
        target = 0
        output = -1

        solution = Solution()
        self.assertEqual(output, solution.search(nums, target))

    def test_no_4(self):
        nums = []
        target = 0
        output = -1

        solution = Solution()
        self.assertEqual(output, solution.search(nums, target))        

if __name__ == '__main__':
    unittest.main()