class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carryUp = 0
        answer = []
        n1 = len(a) - 1
        n2 = len(b) - 1
        while(n1 >= 0) and (n2 >= 0):
            s = carryUp + int(a[n1]) + int(b[n2])
            answer.insert(0, str(s % 2))
            carryUp = 1 if s >= 2 else 0
            n1 -= 1
            n2 -= 1

        if (n1 >= 0):
            answer.insert(0, self.addBinary(str(carryUp), a[0: n1 + 1]))
        elif (n2 >= 0):
            answer.insert(0, self.addBinary(str(carryUp), b[0: n2 + 1]))
        elif (carryUp == 1):
            answer.insert(0, "1")
        return "".join(answer)
            
