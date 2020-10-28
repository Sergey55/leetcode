# Solution fo problem #2 `Add Two Numbers`
#
# Description: ou are given two non-empty linked lists representing 
# two non-negative integers. The digits are stored in reverse order, 
# and each of their nodes contains a single digit. Add the two numbers 
# and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except 
# the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        resultNode = None
        currentNode = None
        
        currentL1Node = l1
        currentL2Node = l2
        
        carry = 0
        
        while(currentL1Node is not None or currentL2Node is not None or carry > 0):
            localSum = 0
            
            if currentL1Node is not None:
                localSum += currentL1Node.val
                
                currentL1Node = currentL1Node.next
                
            if currentL2Node is not None:
                localSum += currentL2Node.val
                
                currentL2Node = currentL2Node.next
                
            localSum += carry
            
            carry = localSum // 10
            
            if resultNode is None:
                resultNode = ListNode(localSum % 10)
                currentNode = resultNode
            else:
                
                currentNode.next = ListNode(localSum % 10)
                currentNode = currentNode.next
            
        return resultNode