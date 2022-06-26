class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        W = len(image[0])

        for row in image:
            L = 0
            R = W - 1
            while(L < R):
                row[L], row[R] = abs(row[R] - 1), abs(row[L] - 1)
                L += 1
                R -= 1
            if (L == R):
                row[L] = abs(row[L] - 1)
        return image
