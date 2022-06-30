# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def convertToList(self, root: Optional[ListNode]) -> List[ListNode]:
        result = []
        while(root):
            nextNode = root.next
            root.next = None
            result.append(root)
            root = nextNode
        return result

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        nums1 = self.convertToList(l1)
        nums2 = self.convertToList(l2)
        result = ListNode(0) # dummy

        carryUp = 0
        idx1 = len(nums1) - 1
        idx2 = len(nums2) - 1
        while idx1 >= 0 and idx2 >= 0:
            node1 = nums1[idx1]
            node2 = nums2[idx2]
            s = node1.val + node2.val + carryUp
            node1.val = s % 10
            carryUp = s // 10

            # [dummy]
            # [dummy] -> [7]
            # [dummy] -> [0] -> [7]
            # [dummy] -> [8] -> [0] -> [7]
            node1.next = result.next
            result.next = node1

            idx1 -= 1
            idx2 -= 1

        rest = nums1 if idx1 >= 0 else nums2
        restIdx = max(idx1, idx2)
        while restIdx >= 0:
            node = rest[restIdx]
            s = node.val + carryUp
            node.val = s % 10
            carryUp = s // 10

            node.next = result.next
            result.next = node

            restIdx -= 1

        if (carryUp == 1):
            result.val = 1
            return result
        else:
            return result.next
