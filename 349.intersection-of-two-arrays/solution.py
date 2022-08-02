class Solution:
    def binarySearch(self, nums: List[int], target: int) -> bool:

        L = 0
        R = len(nums) - 1
        while(L <= R):
            mid = L + (R - L) // 2
            if (nums[mid] == target):
                return True
            elif (nums[mid] < target):
                L = mid + 1
            else:
                R = mid - 1
        return False

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        checked = set()
        nums2.sort()
        matched = []

        for num1 in nums1:
            if num1 in checked:
                continue
            checked.add(num1)

            if (self.binarySearch(nums2, num1)):
                matched.append(num1)
        return matched

        
