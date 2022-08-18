class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = Counter(arr)
        size = len(arr)
        half = size >> 1

        values = sorted(list(counts.values()))
        i = len(values) - 1
        while(half < size):
            size -= values[i]
            i -= 1
        return len(values) - i - 1
