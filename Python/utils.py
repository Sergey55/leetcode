from listnode import ListNode
from typing import List

def linked_list_to_list(lst: ListNode) -> List[int]:
    """Convert LinkedList to Python list
    Args:
        list: Linked list to process
    
    Returns:
        Result Python list
    """
    node = lst
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def to_linked_list(data: List[int]) -> ListNode:
    """Convert Python list to LinkedList
    Args:
        data: Python list
    Returns:
        Result LinkedList
    """
    head = None
    previous = None
    for i in data:
        node = ListNode(i)
        if not head:
            head = node
            previous = node
        elif previous:
            previous.next = node
            previous = node
    return head