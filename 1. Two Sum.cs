/*Solution fo problem #1 `Two Sum`

Description: Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.*/

using System;
using System.Linq;

namespace leetcode.problem1
{
    public class Solution {
        public int[] TwoSum(int[] nums, int target) {
            var dict = nums.Select((x, i) => new { Index = i, Value = x})
                .ToLookup(x => x.Value, x => x.Index);

            for(int i = 0; i < nums.Length; i++)
            {
                var diff = target - nums[i];

                if (dict.Contains(diff) && dict[diff].Any(v => v != i))
                    return new int[] {i, dict[diff].First(v => v != i)};
            }

            return new int[0];
        }
    }
}