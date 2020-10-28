"""Solution for problem #16

Description: Given an array nums of n integers and an integer 
target, find three integers in nums such that the sum is 
closest to target. Return the sum of the three integers. 
You may assume that each input would have exactly one solution.
"""

from typing import List

import unittest

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        left = 0
        right = len(nums) - 1
        
        min_diff = float('inf')
        closest = None

        for i in range(0, len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                s = (nums[left] + nums[right] + nums[i])
                diff = target - s

                if abs(diff) < abs(min_diff):
                    min_diff = target - s
                    closest = s

                if diff > 0:
                    left += 1
                else:
                    right -= 1

            if diff == 0:
                break

        return closest

class TestsForSolution(unittest.TestCase):
    def test_no_1(self):
        input = [-1,2,1,-4]
        target = 1
        output = 2

        solution = Solution()
        self.assertEqual(output, solution.threeSumClosest(input, target))

    def test_no_2(self):
        input = [1,1,1,0]
        target = 100
        output = 3

        solution = Solution()
        self.assertEqual(output, solution.threeSumClosest(input, target))          

if __name__ == '__main__':
    unittest.main()