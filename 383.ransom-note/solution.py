class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rCounts = Counter(ransomNote)
        mCounts = Counter(magazine)
        for rChar in rCounts.keys():
            if (rChar not in mCounts) or (mCounts[rChar] < rCounts[rChar]):
                return False
        return True
