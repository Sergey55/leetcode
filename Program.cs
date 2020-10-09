using System;

namespace leetcode
{
    class Program
    {
        static void Main(string[] args)
        {
            var solution = new leetcode.problem1.Solution();

            var result = solution.TwoSum(new int[] {1, 2, 3}, 5);

            Console.WriteLine(result.ToResult());
        }
    }
}
