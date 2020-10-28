using System;

namespace leetcode
{
    public static class ToResultStringExtensions
    {
        public static string ToResult(this int[] arr)
        {
            return $"[{string.Join(", ", arr)}]";
        }
    }
}