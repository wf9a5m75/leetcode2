class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        appeared = set()
        expects = set()
        for mVal in arr:
            # Ignore the appeared value before except 0
            if ((mVal in appeared) and (mVal != 0)):
                continue

            # If mVal is double of something before,
            # or the value doubled of mVal appeared before,
            # return True
            if (mVal in expects) or ((mVal * 2) in expects):
                return True
            expects.add(mVal) # mVal as M
            expects.add(mVal * 2) # mVal as N
            appeared.add(mVal)
        return False
                
