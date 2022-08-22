class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
    
        # Count up all word frequencies ( space complexity: O(N) )
        freq = Counter(words)

        # compair functiton
        def cmp(wordA: str, wordB: str) -> int:

            # Compairing two words by frequencies
            cntA = freq[wordA]
            cntB = freq[wordB]
            if (cntA != cntB):
                return cntA - cntB

            # Compairing by lexicographical order
            sizeA = len(wordA)
            sizeB = len(wordB)

            for i in range(min(sizeA,  sizeB)):
                if (wordA[i] != wordB[i]):
                    return ord(wordB[i]) - ord(wordA[i])

            return sizeB - sizeA

        results = []
        size = 0
        for word in freq.keys():

            # We sort the results using binary search every time, but if its size beyonds k,
            # remove the smallest one
            # Since the results size never beyonds K,  time complexity is O(n log k)
            L = 0
            R = size - 1
            while(L <= R):
                mid = (L + R) >> 1

                rc = cmp(results[mid], word)
                if (rc > 0):
                    L = mid + 1
                else:
                    R = mid - 1
            results.insert(L, word)
            size += 1

            if (size > k):
                results.pop()
                size -= 1
        return results
