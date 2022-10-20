class Value:
    def __init__(self, value: str, timestamp: int):
        self.value = value
        self.timestamp = timestamp

    def __repr__(self):
        return f"({self.value}, {self.timestamp})"
class TimeMap:

    def __init__(self):
        self.mem = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        newVal = Value(value, timestamp)
        values = self.mem.get(key, [])
        size = len(values)

        L = 0
        R = size - 1
        while(L <= R):
            mid = (L + R) >> 1
            if (values[mid].timestamp <= timestamp):
                L = mid + 1
            else:
                R = mid - 1
        values.insert(L, newVal)

        self.mem[key] = values

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mem:
            return ""

        values = self.mem.get(key, [])
        if (values[-1].timestamp <= timestamp):
            return values[-1].value
        if (values[0].timestamp > timestamp):
            return ""

        size = len(values)
        L = 0
        R = size - 1
        while(L <= R):
            mid = (L + R) >> 1
            if (values[mid].timestamp <= timestamp):
                L = mid + 1
            else:
                R = mid - 1
        return values[R].value


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

"""
test cases

["TimeMap","set","get","get","set","get","get","get","get"]
[[],["foo","bar",2],["foo",2],["foo",3],["foo","bar2",4],["foo",4],["foo",3],["foo",5],["foo",1]]

["TimeMap","set","set","get","get","get","get","get"]
[[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]

["TimeMap","set","set","set","set","get","get","get","get","get","get","set","get","get","get","set","set","set","set","get","get"]
[[],["ctondw","ztpearaw",1],["vrobykydll","hwliiq",2],["gszaw","ztpearaw",3],["ctondw","gszaw",4],["gszaw",5],["ctondw",6],["ctondw",7],["gszaw",8],["vrobykydll",9],["ctondw",10],["vrobykydll","kcvcjzzwx",11],["vrobykydll",12],["ctondw",13],["vrobykydll",14],["ztpearaw","zondoubtib",15],["kcvcjzzwx","hwliiq",16],["wtgbfvg","vrobykydll",17],["hwliiq","gzsiivks",18],["kcvcjzzwx",19],["ztpearaw",20]]

["TimeMap","set","get","get","set","get","get","get","set","set","set","get"]
[[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5],["foo",1],["foo","bar3",8],["foo","bar4",10],["foo","bar5",15],["foo",12]]
"""
