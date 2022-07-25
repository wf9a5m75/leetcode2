# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        buffer = []
        p = head
        while(p):
            currNext = p.next
            buffer.append(p)
            p.next = None
            p = currNext

        L = 1
        R = len(buffer) - 1

        tail = buffer[0]
        while(L < R):
            tail.next = buffer[R]
            buffer[R].next = buffer[L]
            tail = buffer[L]
            L += 1
            R -= 1
        if (L == R):
            tail.next = buffer[L]
