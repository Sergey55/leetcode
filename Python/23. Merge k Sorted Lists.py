"""Solution for problem #23 `Merge k Sorted Lists`

Description: You are given an array of k linked-lists lists, 
each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""

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
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        result = []
        head = current = ListNode(0)

        for l in lists:
            while l:
                result.append(l.val)
                l = l.next

        for v in sorted(result):
            current.next = ListNode(v)
            current = current.next

        return head.next

class TestsForSolution(unittest.TestCase):
    def test_no_1(self):
        input = [[1,4,5],[1,3,4],[2,6]]
        output = [1,1,2,3,4,4,5,6]

        input = [to_linked_list(l) for l in input]

        solution = Solution()
        self.assertEqual(output, linked_list_to_list(solution.mergeKLists(input)))

    def test_no_2(self):
        input = []
        output = []

        input = [to_linked_list(l) for l in input]

        solution = Solution()
        self.assertEqual(output, linked_list_to_list(solution.mergeKLists(input)))

    def test_no_3(self):
        input = [[]]
        output = []

        input = [to_linked_list(l) for l in input]

        solution = Solution()
        self.assertEqual(output, linked_list_to_list(solution.mergeKLists(input)))

if __name__ == '__main__':
    unittest.main()