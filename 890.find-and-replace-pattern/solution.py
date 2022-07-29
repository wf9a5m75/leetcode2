class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        size = len(pattern)
        results = []
        for word in words:
            p2w = {}
            w2p = {}

            matched = True
            for i in range(size):
                wchar = word[i]
                pchar = pattern[i]

                if pchar in p2w:
                    expectW = p2w[pchar]
                    expectP = pchar
                elif wchar in w2p:
                    expectP = w2p[wchar]
                    expectW = wchar
                else:
                    w2p[wchar] = pchar
                    p2w[pchar] = wchar
                    continue

                if (wchar != expectW) or (pchar != expectP):
                    matched = False
                    break
            if matched:
                results.append(word)
        return results
