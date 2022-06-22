class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mem1 = Counter(nums1)
        mem2 = Counter(nums2)
        result = []
        for num in mem1.keys():
            if num in mem2:
                result += [num] * min(mem1[num], mem2[num])
        return result
