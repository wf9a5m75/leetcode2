class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        results = []
        cnt3 = cnt5 = 1
        for i in range(1, n + 1):
            if (cnt3 == 3) or (cnt5 == 5):
                word = ""
                if (cnt3 == 3):
                    cnt3 = 0
                    word = "Fizz"
                if (cnt5 == 5):
                    cnt5 = 0
                    word += "Buzz"
            else:
                word = str(i)
            results.append(word)
            cnt3 += 1
            cnt5 += 1
        return results
                    
