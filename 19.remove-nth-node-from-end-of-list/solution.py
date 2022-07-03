# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total = 0

        footSteps = [head]
        slow = fast = head
        if (fast.next):
            fast = fast.next
            total = 1

        while(fast):
            slow = slow.next
            fast = fast.next

            total += 1
            if (fast):
                footSteps.append(fast)
                fast = fast.next
                total += 1


        pos = total - n

        if (pos == 0):
            # case: the target node is located at the head
            return head.next

        idx = (pos // 2)
        parent = footSteps[idx]

        if (pos % 2 == 0):
            parent = footSteps[idx - 1]
            parent = parent.next

        parent.next = parent.next.next
        return head

        
