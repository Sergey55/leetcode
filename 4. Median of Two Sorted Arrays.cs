/* Solution for problem #4 `Median of Two Sorted Arrays`

Description: Given two sorted arrays nums1 and nums2 of size m and n 
respectively, return the median of the two sorted arrays.
*/
using System;
using System.Linq;

namespace leetcode.problem4
{
    public class Solution {
        public double FindMedianSortedArrays(int[] nums1, int[] nums2) {
            var arr = nums1.Union(nums2).OrderBy(v => v).ToArray();

            var center = arr.Length / 2;

            return ((center % 1 - 0.5 < 0.001)) ? 
                arr[(int)(center)] : 
                (arr[(int)(center) - 1] + arr[(int)(center)]) / 2;
        }        
    }
}