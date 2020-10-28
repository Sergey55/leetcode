"""Solution for problem #19 `Remove Nth Node From End of List`

Description: Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?"""

import unittest

from typing import List
from listnode import ListNode
from utils import to_linked_list, linked_list_to_list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        size = 1
        current = previous = head

        while current.next:
            size += 1
            current = current.next

            if size > n + 1:
                previous = previous.next

        if size == n:
            return head.next
        else:
            previous.next = previous.next.next
            return head

class TestsForSolution(unittest.TestCase):
    def test_no_0_1(self):
        inpt = [1, 2, 3, 4, 5]

        self.assertEqual(inpt, linked_list_to_list(to_linked_list(inpt)))

    def test_no_0_2(self):
        inpt = [1, 2]

        self.assertEqual(inpt, linked_list_to_list(to_linked_list(inpt)))        

    def test_no_1(self):
        input = to_linked_list([1,2,3,4,5])
        n = 2
        output = [1,2,3,5]

        solution = Solution()
        self.assertEqual(output, linked_list_to_list(solution.removeNthFromEnd(input, n)))

    def test_no_2(self):
        input = to_linked_list([1])
        n = 1
        output = []

        solution = Solution()
        self.assertEqual(output, linked_list_to_list(solution.removeNthFromEnd(input, n)))

    def test_no_3(self):
        input = to_linked_list([1,2])
        n = 1
        output = [1]

        solution = Solution()
        self.assertEqual(output, linked_list_to_list(solution.removeNthFromEnd(input, n)))

    def test_no_4(self):
        input = to_linked_list([1,2])
        n = 2
        output = [2]

        solution = Solution()
        self.assertEqual(output, linked_list_to_list(solution.removeNthFromEnd(input, n)))


if __name__ == '__main__':
    unittest.main()