"""Solution for problem #27. Remove Element

Description: Given an array nums and a value val, remove all instances of 
that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying 
the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond 
the new length.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means a modification 
to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeElement(nums, val);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""

import unittest

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        idx = 0

        while idx < len(nums):
            if nums[idx] == val:
                nums.pop(idx)
            else:
                idx += 1

        return len(nums)

class TestsForSolution(unittest.TestCase):
    def test_no_1(self):
        input = [3,2,2,3]
        val = 2
        output = 2

        solution = Solution()
        self.assertEqual(output, solution.removeElement(input, val))

    def test_no_2(self):
        input = [0,1,2,2,3,0,4,2]
        val = 2
        output = 5

        solution = Solution()
        self.assertEqual(output, solution.removeElement(input, val))        

if __name__ == '__main__':
    unittest.main()