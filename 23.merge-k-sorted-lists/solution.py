# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if (lists is None) or (len(lists) == 0):
            return None

        mem = {}
        for linkList in lists:
            head = linkList
            while(head):
                prev = start = head
                while(head) and (start.val == head.val):
                    prev = head
                    head = head.next

                if (start.val in mem):
                    mem[start.val]["tail"].next = start
                    mem[start.val]["tail"] = prev
                else:
                    mem[start.val] = {
                        "head": start,
                        "tail": prev
                    }

        result = tail = ListNode(-10000) # dummy
        kinds = sorted(mem.keys())
        for kind in kinds:
            node = mem[kind]
            tail.next = node["head"]
            tail = node["tail"]

        return result.next
            
