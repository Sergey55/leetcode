"""Solution for problem #4 `3Sum`

Description: Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Notice that the solution set must not contain duplicate quadruplets.
"""
import unittest

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            res = []
            if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
                return res
            if k == 2:
                return twoSum(nums, target)
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for _, set in enumerate(kSum(nums[i + 1:], target - nums[i], k - 1)):
                        res.append([nums[i]] + set)
            return res

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            lo, hi = 0, len(nums) - 1
            while (lo < hi):
                sum = nums[lo] + nums[hi]
                if sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                    lo += 1
                elif sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
            return res

        if len(nums) < 4:
            return []

        nums.sort()

        return kSum(nums, target, 4)

class TestsForSolution(unittest.TestCase):
    def test_no_1(self):
        input = [1,0,-1,0,-2,2]
        target = 0
        output = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

        solution = Solution()
        self.assertEqual(output, solution.fourSum(input, target))

    def test_no_2(self):
        input = []
        target = 0
        output = []

        solution = Solution()
        self.assertEqual(output, solution.fourSum(input, target))

if __name__ == '__main__':
    unittest.main();