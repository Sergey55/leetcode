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

        nums.sort()

        results = []
        resultsSet = set()

        for i in range(ln - 2):
            v = nums[i]

            left = i + 1
            right = ln - 1

            while left < right:
                s = nums[left] + nums[right] + v

                if (s == 0) and (v, nums[left], nums[right]) not in resultsSet:
                    results.append([v, nums[left], nums[right]])
                    resultsSet.add((v, nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1

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