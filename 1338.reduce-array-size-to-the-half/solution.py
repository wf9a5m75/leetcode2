class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        rest = len(arr)
        if (rest == 1):
            return 1

        half = rest >> 1
        counts = Counter(arr)
        keys = list(counts.keys())
        self.quickSort(keys, 0, len(keys) - 1, lambda x: counts[x])

        cnt = 0
        for key in keys:
            cnt += 1
            rest -= counts[key]
            if rest <= half:
                return cnt

        return cnt

    def quickSort(self, arr: List[int], start: int, end: int, getVal: Callable[[int], int]) -> None:
        if (start >= end):
            return

        pivot = getVal(arr[start])
        L = start
        R = end
        while(L <= R):

            # In order to reverse sort, the conditions are also reversed.
            while(L < end) and (getVal(arr[L]) > pivot):
                L += 1
            while(start < R) and (pivot > getVal(arr[R])):
                R -= 1

            if (L > R):
                break
            arr[L], arr[R] = arr[R], arr[L]
            L += 1
            R -= 1

        self.quickSort(arr, start, L - 1, getVal)
        self.quickSort(arr, L, end, getVal)
