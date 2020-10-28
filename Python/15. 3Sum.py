"""Solution for problem #15 `3Sum`

Description: Given an array nums of n integers, are there elements 
a, b, c in nums such that a + b + c = 0? Find all unique triplets in 
the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets."""

from typing import List

import unittest

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ln = len(nums)

        #if shorter then 3 return empty list
        if ln < 3:
            return []

        results = []

        nums.sort()

        lookup = {(a + b): (ai, bi) for ai, a in enumerate(nums) for bi, b in enumerate(nums) if ai != bi}

        for i, v in enumerate(nums):
            if v in lookup:
                left, right = lookup[v]

                if left != i and right != i:
                    results.append([i, nums[left], nums[right]])

        return results
        
class TestsForSolution(unittest.TestCase):
    def test_no_1(self):
        input = [-1,0,1,2,-1,-4]
        output = [[-1,-1,2],[-1,0,1]]

        solution = Solution()
        self.assertEqual(output, solution.threeSum(input))

    def test_no_2(self):
        input = []
        output = []

        solution = Solution()
        self.assertEqual(output, solution.threeSum(input))

    def test_no_3(self):
        input = [0]
        output = []

        solution = Solution()
        self.assertEqual(output, solution.threeSum(input))        

if __name__ == '__main__':
    unittest.main()