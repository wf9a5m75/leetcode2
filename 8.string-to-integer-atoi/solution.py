class Solution:
    def myAtoi(self, s: str) -> int:
        global signal, intNum, INT_MAX, allowLeadingSpace, allowSignal

        signal = None
        intNum = 0
        INT_MAX = 2**31
        allowLeadingSpace = True
        allowSignal = True

        def action_signal(char: str) -> bool:
            global signal, allowLeadingSpace, allowSignal
            if allowSignal == False:
                return False

            if signal is not None:
                return False
            allowLeadingSpace = False
            signal = char
            return True

        def action_number(digit: int) -> bool:
            global intNum, INT_MAX, allowLeadingSpace, allowSignal

            allowLeadingSpace = False
            allowSignal = False
            intNum = min(intNum * 10 + digit, INT_MAX)
            return True

        def action_space(char: str) -> bool:
            global allowLeadingSpace
            return allowLeadingSpace

        actions = {
            "+": action_signal,
            "-": action_signal,
            "0": lambda char: action_number(0),
            "1": lambda char: action_number(1),
            "2": lambda char: action_number(2),
            "3": lambda char: action_number(3),
            "4": lambda char: action_number(4),
            "5": lambda char: action_number(5),
            "6": lambda char: action_number(6),
            "7": lambda char: action_number(7),
            "8": lambda char: action_number(8),
            "9": lambda char: action_number(9),
            " ": action_space,
        }
        for char in s:
            if (char not in actions) or (actions[char](char) == False):
                break
        if signal == "+":
            intNum = min(intNum, INT_MAX - 1)
        elif signal == "-":
            intNum *= -1
        else:
            intNum = min(intNum, INT_MAX - 1)
        return intNum
