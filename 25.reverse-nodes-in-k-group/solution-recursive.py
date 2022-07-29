# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head

        # Find the k + 1 node
        cnt = 0
        while(curr) and (cnt < k):
            curr = curr.next
            cnt += 1

        if (cnt == k):
            curr = self.reverseKGroup(curr, k)

            while(cnt > 0):
                headNext = head.next
                head.next = curr
                curr = head
                head = headNext
                cnt -= 1
            head = curr

        return head
        
