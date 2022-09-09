class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x: (-x[0], x[1]))

        ans = 0
        curr_max = 0
        for _, defense in properties:
            if defense < curr_max:
                ans += 1
            else:
                curr_max = defense
        return ans
