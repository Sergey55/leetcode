"""Solution or problem #25. Reverse Nodes in k-Group

Description: Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not 
a multiple of k then left-out nodes, in the end, should remain as it is.

Follow up:

 * Could you solve the problem in O(1) extra memory space?
 * You may not alter the values in the list's nodes, only nodes itself may be changed.

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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head        

        self.head = ListNode(0, head)

        cur, nxt = self.head, self.head
        counter = 0

        while nxt.next:
            if counter < (k - 1):
                nxt = nxt.next
                counter += 1
            else:
                a, b, c, d  = cur.next, nxt, nxt.next, nxt.next.next
                
                # print(f'cur: {cur}, next: {nxt}, a: {a}, b: {b}, c: {c}, d: {d}')
                cur.next, c.next, a.next, a.next = c, a, d, d

                cur, nxt = a, a
                counter = 0

        
        return self.head.next

class TestsForSolution(unittest.TestCase):
    def test_no_1(self):
        head = to_linked_list([1,2,3,4,5])
        k = 2
        output = [2,1,4,3,5]

        solution = Solution()
        self.assertEqual(output, linked_list_to_list(solution.reverseKGroup(head, k)))

    def test_no_2(self):
        head = to_linked_list([1,2,3,4,5])
        k = 3
        output = [3,2,1,4,5]

        solution = Solution()
        self.assertEqual(output, linked_list_to_list(solution.reverseKGroup(head, k)))

    def test_no_3(self):
        head = to_linked_list([1,2,3,4,5])
        k = 1
        output = [1,2,3,4,5]

        solution = Solution()
        self.assertEqual(output, linked_list_to_list(solution.reverseKGroup(head, k)))

    def test_no_4(self):
        head = to_linked_list([1])
        k = 1
        output = [1]

        solution = Solution()
        self.assertEqual(output, linked_list_to_list(solution.reverseKGroup(head, k)))

    def test_no_4(self):
        head = to_linked_list([1, 2, 3, 4])
        k = 4
        output = [4, 3, 2, 1]

        solution = Solution()
        self.assertEqual(output, linked_list_to_list(solution.reverseKGroup(head, k)))

    def test_no_5(self):
        head = to_linked_list([1, 2, 3, 4, 5])
        k = 5
        output = [5, 4, 3, 2, 1]

        solution = Solution()
        self.assertEqual(output, linked_list_to_list(solution.reverseKGroup(head, k)))         

if __name__ == '__main__':
    unittest.main()