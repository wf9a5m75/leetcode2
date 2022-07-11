class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = len(num1) - 1
        n2 = len(num2) - 1

        carryUp = 0
        result = ""
        while(n1 > -1) or (n2 > -1):
            digit1 = 0
            if n1 > -1:
                digit1 = int(num1[n1])
                n1 -= 1

            digit2 = 0
            if n2 > -1:
                digit2 = int(num2[n2])
                n2 -= 1

            s = digit1 + digit2 + carryUp
            result = f"{s % 10}{result}"
            carryUp = s // 10

        if (carryUp == 1):
            result = f"1{result}"

        return result
