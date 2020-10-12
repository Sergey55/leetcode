# Solution for problem #3 `Longest Substring Without Repeating Characters`
#
# Desciption: Given a string s, find the length of the longest substring without 
# repeating characters.
#
# Ex 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
import unittest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        maxVal = 0
        count = 0
        
        currentCharacters = ''
        
        for c in s:            
            if c in currentCharacters:
                if maxVal < count:
                    maxVal = count
                
                idx = currentCharacters.index(c)
                currentCharacters = currentCharacters[idx + 1:]
                
                currentCharacters += c
                count = len(currentCharacters)
            else:
                currentCharacters += c
                count += 1
                
        return max(maxVal, count)

class TestsForSolution(unittest.TestCase):

    def test_no_1(self):
        inputString = "abcabcbb"
        output = 3

        solution = Solution()
        self.assertEqual(output, solution.lengthOfLongestSubstring(inputString))

    def test_no_2(self):
        inputString = "bbbbb"
        output = 1

        solution = Solution()
        self.assertEqual(output, solution.lengthOfLongestSubstring(inputString))

    def test_no_3(self):
        inputString = "pwwkew"
        output = 3

        solution = Solution()
        self.assertEqual(output, solution.lengthOfLongestSubstring(inputString))

    def test_no_4(self):
        inputString = ""
        output = 0

        solution = Solution()
        self.assertEqual(output, solution.lengthOfLongestSubstring(inputString))

if __name__ == '__main__':
    unittest.main()