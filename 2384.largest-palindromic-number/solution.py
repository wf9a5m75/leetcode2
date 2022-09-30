class Solution:
    def largestPalindromic(self, num: str) -> str:
        # Bit flags for preventing the leading zeros.
        # 0bBBBBBBBBBB
        #   9876543210
        kinds = 0

        # Counting up the number of digits
        counts = [0] * 10
        for c in num:
            idx = int(c)
            counts[idx] += 1

            # Sets 1 on the bit flag
            kinds |= 1 << idx

        # Find the center digit which is the largest digit and appears odd times.
        mid = ""
        for i in range(9, -1, -1):
            if (counts[i] & 1) == 1:

                # Pick the only the largest digit
                if mid == "":
                    mid = str(i)

                # converts to even times
                counts[i] -= 1

                # If there is no "i" digit, clear the bit flag
                if counts[i] == 0:
                    kinds = kinds ^ (1 << i)

        # The each bit of the kinds variable denotes
        # what digits are still available.
        #
        # If there is only "0" digit, kinds = 0b0000000001.
        # If there is no digit, kinds = 0b0000000000
        #
        # Therefore, we check the digits from 2 to 9 using bit masking (0x3FE = 0b1111111110),
        # then if it is greater than 0, it means there is something available.
        prefix = ""
        suffix = ""
        if (kinds & 0x3FE) > 0:
            for i in range(10):
                cnt = counts[i] >> 1
                if cnt > 0:
                    tmp = str(i) * cnt
                    prefix = tmp + prefix
                    suffix = suffix + tmp

        result = prefix + mid + suffix
        return "0" if result == "" else result
