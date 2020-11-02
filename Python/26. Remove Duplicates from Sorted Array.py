"""Solution for problem #26. Remove Duplicates from Sorted Array

Description: Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""
from typing import List

import unittest

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1

        while idx < len(nums):
            if nums[idx] == nums[idx - 1]:
                nums.pop(idx)
            else:
                idx += 1

        return len(nums)

class TestsForSolution(unittest.TestCase):
    def test_no_1(self):
        input = [1,1,2]
        output = 2

        solution = Solution()
        self.assertEqual(output, solution.removeDuplicates(input))

    def test_no_2(self):
        input = [0,0,1,1,1,2,2,3,3,4]
        output = 5

        solution = Solution()
        self.assertEqual(output, solution.removeDuplicates(input))

if __name__ == '__main__':
    unittest.main()