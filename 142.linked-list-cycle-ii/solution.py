# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        f = s = head
        if f is None:
            return None

        while True:
            s = s.next
            f = f.next
            if (f is None):
                return None
            f = f.next
            if (f is None):
                return None
            if (s == f):
                break

        f = head
        while(f != s):
            f = f.next
            s = s.next
        return f
            
