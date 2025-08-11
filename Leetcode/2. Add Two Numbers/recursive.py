"""
Time Complexity: O(max(N, M))
    - O(max(N, m)) time to reach every l1, l2
Space Complexity: O(max(N, M))
    - max(N, M) stored in result
    - recursion stack up to depth n
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def _addNumbers(self, l1, l2, carry):
        if not l1 and not l2 and not carry:
            return None

        sum = carry
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next
        carry = sum // 10

        node = ListNode(sum % 10)
        node.next = self._addNumbers(l1, l2, carry)
        return node
 
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self._addNumbers(l1, l2, 0)