""" Solution for proble 24. Swap Nodes in Pairs

Description: Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes. Only nodes itself may be changed
"""

import unittest

from listnode import ListNode
from utils import linked_list_to_list, to_linked_list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        self.head = ListNode(0, head)
        cur = self.head

        while cur.next and cur.next.next:
            a, b, c = cur.next, cur.next.next, cur.next.next.next

            cur.next, b.next, a.next, cur = b, a, c, a

        return self.head.next


class TestsForSolution(unittest.TestCase):
    def test_no_1(self):
        input = to_linked_list([1,2,3,4])
        expectedOutput = [2,1,4,3]

        solution = Solution()
        output = solution.swapPairs(input)
        self.assertEqual(expectedOutput, linked_list_to_list(output))

    def test_no_2(self):
        input = to_linked_list([])
        expectedOutput = []

        solution = Solution()
        output = solution.swapPairs(input)
        self.assertEqual(expectedOutput, linked_list_to_list(output))

    def test_no_3(self):
        input = to_linked_list([1])
        expectedOutput = [1]

        solution = Solution()
        output = solution.swapPairs(input)
        self.assertEqual(expectedOutput, linked_list_to_list(output))

if __name__ == '__main__':
    unittest.main()