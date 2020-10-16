"""Solution for problem #11 `Container With Most Water`

Given n non-negative integers a1, a2, ..., an , where each 
represents a point at coordinate (i, ai). n vertical lines 
are drawn such that the two endpoints of the line i is at 
(i, ai) and (i, 0). Find two lines, which, together with the 
x-axis forms a container, such that the container contains 
the most water.

Notice:
    that you may not slant the container.
"""

import unittest

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:

        if len(height) == 2:
            return min(height)

        maxArea = 0
        left = 0
        right = len(height) - 1

        while(left != right):
            if height[left] > height[right]:
                area = height[right] * (right - left)
                right -= 1
            else:
                area = height[left] * (right - left)
                left += 1
            
            if maxArea < area:
                maxArea = area

        return maxArea

class TestsForSolution(unittest.TestCase):

    def test_no_1(self):
        input = [1,8,6,2,5,4,8,3,7]
        output = 49

        solution = Solution()
        self.assertEqual(output, solution.maxArea(input))

    def test_no_2(self):
        input = [1, 1]
        output = 1

        solution = Solution()
        self.assertEqual(output, solution.maxArea(input))

    def test_no_3(self):
        input = [4,3,2,1,4]
        output = 16

        solution = Solution()
        self.assertEqual(output, solution.maxArea(input))

    def test_no_4(self):
        input = [1,2,1]
        output = 2

        solution = Solution()
        self.assertEqual(output, solution.maxArea(input))

if __name__ == '__main__':
    unittest.main()