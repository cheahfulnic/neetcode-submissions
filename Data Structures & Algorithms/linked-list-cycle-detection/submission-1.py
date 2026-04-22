# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise = head
        hare = head

        while tortoise is not None and hare is not None:
            if tortoise.next is None or hare.next is None:
                return False
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return True
        return False