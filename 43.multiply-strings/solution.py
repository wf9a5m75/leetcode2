class Solution:
    @lru_cache
    def sum(self, num1: str, num2: str) -> str:
        orgN1 = num1
        orgN2 = num2

        n1 = len(num1) - 1
        n2 = len(num2) - 1
        answer = []

        carryUp = 0
        while(n1 >= 0) and (n2 >= 0):
            s = int(num1[n1]) + int(num2[n2]) + carryUp
            answer.insert(0, str(s % 10))
            carryUp = s // 10
            n1 -= 1
            n2 -= 1

        if (n1 >= 0):
            restResult = self.sum(num1[:n1 + 1], str(carryUp))
            answer.insert(0, restResult)
        elif (n2 >= 0):
            restResult = self.sum(num2[:n2 + 1], str(carryUp))
            answer.insert(0, restResult)
        elif (carryUp > 0):
            answer.insert(0, str(carryUp))
        return "".join(answer)

    def multiply(self, num1: str, num2: str) -> str:
        answer = []
        mem = {
            "0" : "0",
            "1" : num1
        }

        prev = num1
        for i in range(2, 10):
            prev = self.sum(prev, num1)
            mem[ str(i) ] = prev

        carryUp = "0"
        prev = "0"
        n2 = len(num2) - 1
        while(n2 >= 0):
            s = self.sum(mem[num2[n2]], carryUp)
            answer.insert(0, s[-1])
            lenS = len(s)
            carryUp = s[0:lenS - 1]
            n2 -= 1

        if (carryUp != "0") and (carryUp != ""):
            answer.insert(0, carryUp)

        # remove leading zeros
        while(len(answer) > 1) and (answer[0] == "0"):
            answer.pop(0)

        return "".join(answer)
