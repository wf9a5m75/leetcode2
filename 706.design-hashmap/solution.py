class KeyValue:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value

#
# Space complexity: O(kind of keys)
# Time complexity: O(log N)
#
class MyHashMap:

    def __init__(self):
        self.mem = [[] for _ in range(13)]

    def put(self, key: int, value: int) -> None:
        hashKey = self._hashKey(key)

        pos = self._find(key)

        if (0 <= pos < len(self.mem[hashKey])):
            if (self.mem[hashKey][pos].key == key):
                self.mem[hashKey][pos].value = value
            else:
                self.mem[hashKey].insert(pos, KeyValue(key, value))
        else:
            self.mem[hashKey].append(KeyValue(key, value))


    def get(self, key: int) -> int:
        pos = self._find(key)
        hashKey = self._hashKey(key)

        if (0 <= pos < len(self.mem[hashKey])):
            if (self.mem[hashKey][pos].key == key):
                return self.mem[hashKey][pos].value
        return -1



    def remove(self, key: int) -> None:
        pos = self._find(key)
        hashKey = self._hashKey(key)

        if (0 <= pos < len(self.mem[hashKey])):
            if (self.mem[hashKey][pos].key == key):
                self.mem[hashKey].pop(pos)


    def _find(self, key: int) -> int:
        hashKey = self._hashKey(key)

        L = 0
        R = len(self.mem[hashKey])
        while(L < R):
            mid = (L + R) >> 1
            if (self.mem[hashKey][mid].key < key):
                L = mid + 1
            else:
                R = mid
        return L

    def _hashKey(self, key: int) -> int:
        return key % 13



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
