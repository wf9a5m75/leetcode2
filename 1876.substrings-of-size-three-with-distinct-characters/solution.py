class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        size = len(s)
        if (size < 3):
            return 0

        s = list(s)
        result = 0

        s1 = s[0]
        s2 = s[1]
        s3 = s[2]
        dupS1S2 = s1 == s2
        dupS2S3 = s2 == s3
        result = 1 if (not dupS1S2) and (not dupS2S3) and (s1 != s3) else 0

        for i in range(3, size):
            dupS1S2 = dupS2S3
            s1, s2 = s2, s3

            s3 = s[i]
            dupS2S3 = s2 == s3

            result = result + (1 if (not dupS1S2) and (not dupS2S3) and (s1 != s3) else 0)
        return result
