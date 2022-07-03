# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        if (fast.next):
            fast = fast.next
        else:
            return slow

        while(fast != None):
            slow = slow.next
            fast = fast.next
            if (fast):
                fast = fast.next
        return slow
