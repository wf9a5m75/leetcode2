class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = Counter(s)
        tCount = Counter(t)

        for sChar in sCount.keys():
            if (sChar not in tCount) or (tCount[sChar] != sCount[sChar]):
                return False
            del tCount[sChar]

        return (len(tCount) == 0)
