class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        counts = Counter(secret)
        recheck = []
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                counts[secret[i]] -= 1
            else:
                recheck.append(guess[i])

        for digit in recheck:
            if counts.get(digit, 0) > 0:
                cows += 1
                counts[digit] -= 1
        return f"{bulls}A{cows}B"
            
