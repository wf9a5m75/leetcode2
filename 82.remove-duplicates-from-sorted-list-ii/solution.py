# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None):
            return None

        # dummy head
        tail = result = ListNode(-1000)

        # True if the tail.val is duplicated
        canReplaceTail = False

        while(head != None):
            if (tail.val != head.val):
                # If the canReplaceTail is True,
                # we need to replace the tail node.
                if (canReplaceTail):
                    tail.val = head.val
                    canReplaceTail = False
                else:
                    tail.next = head
                    tail = tail.next
            else:
                canReplaceTail = True
            head = head.next

        tail.next = None

        # The case for the last value is duplicated.
        # We need to remove the tail element, in that case.
        if (canReplaceTail):
            head = result
            while(head.next != tail):
                head = head.next
            head.next = None

        return result.next
