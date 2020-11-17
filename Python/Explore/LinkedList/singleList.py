from structs import ListNode

import unittest

def addNode(node: ListNode, new: ListNode, position: int) -> ListNode:

    head = ListNode(-1, node)

    pos = 0
    prev, cur = head, head.next

    while cur and pos < position:
        prev, cur = cur, cur.next
        pos += 1

    if pos == position:
        prev.next = new
        new.next = cur

    return head.next

class Tests(unittest.TestCase):
    def test_addition_to_the_first_position(self):
        node = ListNode(1, ListNode(2))
        new = ListNode(0)

        position = 0

        result = addNode(node, new, position)
        
        self.assertEqual(0, result.val)
        self.assertEqual(1, result.next.val)
        self.assertEqual(2, result.next.next.val)

    def test_insert_node_between_two_nodes(self):
        node = ListNode(1, ListNode(3))
        new = ListNode(2)

        position = 1

        result = addNode(node, new, position)

        self.assertEqual(1, result.val)
        self.assertEqual(2, result.next.val)
        self.assertEqual(3, result.next.next.val)

    def test_insert_to_last_position(self):
        node = ListNode(1, ListNode(2))
        new = ListNode(3)

        position = 2
    
        result = addNode(node, new, position)

        self.assertEqual(1, result.val)
        self.assertEqual(2, result.next.val)
        self.assertEqual(3, result.next.next.val)        

if __name__ == '__main__':
    unittest.main()