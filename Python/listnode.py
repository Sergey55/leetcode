# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        nextValue = 'None'  if not self.next else str(self.next.val)
        return str(f'[{self.val}->{nextValue}]')