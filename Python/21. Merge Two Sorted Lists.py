"""Solution for problem #20 `Merge Two Sorted Lists`

Description: Merge two sorted linked lists and return it as a 
new sorted list. The new list should be made by splicing together the nodes of the first two lists.
"""
import unittest

from listnode import ListNode
from utils import to_linked_list, linked_list_to_list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1

        current, current_l1, current_l2 = self.getNodeWithMinValue(l1, l2)
        head = current

        while current_l1 or current_l2:
            current.next, current_l1, current_l2 = self.getNodeWithMinValue(current_l1, current_l2)
            current = current.next

        return head
    
    def getNodeWithMinValue(self, l1: ListNode, l2: ListNode):
        if l1 and l2:
            if l1.val < l2.val:
                return l1, l1.next, l2
            else:
                return l2, l1, l2.next
        elif l1:
            return l1, l1.next, l2
        elif l2:
            return l2, l1, l2.next
        else:
            return None, None, None

class TestsForSolution(unittest.TestCase):
    def test_no_1(self):
        l1, l2 = [1, 2, 4], [1, 3, 4]
        output = [1, 1, 2, 3, 4, 4]

        solution = Solution()
        self.assertEqual(output, linked_list_to_list(solution.mergeTwoLists(to_linked_list(l1), to_linked_list(l2))))

    def test_no_2(self):
        l1, l2 = [], []
        output = []

        solution = Solution()
        self.assertEqual(output, linked_list_to_list(solution.mergeTwoLists(to_linked_list(l1), to_linked_list(l2))))

    def test_no_3(self):
        l1, l2 = [], [0]
        output = [0]

        solution = Solution()
        self.assertEqual(output, linked_list_to_list(solution.mergeTwoLists(to_linked_list(l1), to_linked_list(l2))))

if __name__ == '__main__':
    unittest.main()