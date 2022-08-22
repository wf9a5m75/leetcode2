# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode(0)
        even = ListNode(0)

        lists = [odd, even]
        idx = 0
        while(head):
            lists[idx].next = head
            lists[idx] = lists[idx].next
            idx = (idx + 1) & 1
            head = head.next
        lists[0].next = even.next
        lists[1].next = None
        return odd.next
