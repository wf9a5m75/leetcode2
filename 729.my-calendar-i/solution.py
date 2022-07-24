class Period:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __str__(self):
        return f"({self.start} - {self.end})"

class MyCalendar:

    def __init__(self):
        # insert dummy terminal schedules
        self.schedules = [Period(-2, -1), Period(10**10, 10**10 + 1)]


    def book(self, start: int, end: int) -> bool:
        size = len(self.schedules)

        L = 0
        R = size

        while(L <= R):
            mid = (L + R) >> 1
            schedule = self.schedules[mid]
            if (schedule.end > start):
                R = mid - 1
            else:
                L = mid + 1

        before = self.schedules[R]
        after = self.schedules[L]
        #print(before, after, L, R)
        if (before.end <= start) and (end <= after.start):
            self.schedules.insert(L, Period(start, end))
            return True
        else:
            return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
