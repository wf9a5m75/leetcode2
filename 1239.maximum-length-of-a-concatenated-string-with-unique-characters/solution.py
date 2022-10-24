class Solution:
    def maxLength(self, arr: List[str]) -> int:
        size = len(arr)

        @cache
        def backtrack(idx: int, maskSoFar: int) -> int:
            if (idx == size):
                return 0

            result = 0
            for j in range(idx, size):
                result1 = maskSoFar | masks[j]
                result2 = maskSoFar ^ masks[j]
                if (result1 != result2):
                    continue
                result = max(result, backtrack(j + 1, result1) + len(arr[j]))
            return result


        masks = []
        for i, txt in enumerate(arr):
            mask = 0
            for char in txt:
                flag = 1 << (ord(char) - 97)
                if (mask & flag) != 0:
                    mask = 0
                    arr[i] = ""
                    break

                mask |= flag
            masks.append(mask)

        result = backtrack(0, 0)

        return result
