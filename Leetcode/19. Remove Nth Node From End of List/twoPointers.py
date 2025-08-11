"""
Time Complexity: O(n)
Space Complexity: O(n)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow, fast, i = dummy, dummy, 0
        while i <= n and fast:
            fast = fast.next
            i += 1
        
        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        
        return dummy.next