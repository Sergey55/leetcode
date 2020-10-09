# Solution fo problem #1 `Two Sum`
#
# Description: Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
#
# You can return the answer in any order.

import unittest

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {v: i for i, v in enumerate(nums)}
        
        for i in range(len(nums)):
            if d.__contains__(target - nums[i]) and d[target - nums[i]] != i:
                return [i, d[target - nums[i]]]
                
        return []

class UnitTestForSolution(unittest.TestCase):

    def test_num_1(self):
        input_list = [2, 7, 11, 15]
        target = 9

        result = Solution().twoSum(input_list, target)
        self.assertEqual(result, [0, 1])

    def test_num_2(self):
        input_list = [3, 2, 4]
        target = 6

        result = Solution().twoSum(input_list, target)
        self.assertEqual(result, [1, 2])

if __name__ == '__main__':
    unittest.main()
