# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        ptrA = headA
        ptrB = headB
        while(ptrA):
            ptrA.val = -ptrA.val
            ptrA = ptrA.next

        while(ptrB) and (ptrB.val >= 0):
            ptrB = ptrB.next

        intersection = ptrB

        ptrA = headA
        while(ptrA):
            ptrA.val = -ptrA.val
            ptrA = ptrA.next

        return intersection
