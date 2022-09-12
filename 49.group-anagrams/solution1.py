class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mem = {}

        for word in strs:
            counts = Counter(word)

            key = ""
            chars = sorted(counts.keys())
            for char in chars:
                key += f"{char}{counts[char]}"

            if key not in mem:
                mem[key] = []
            mem[key].append(word)

        results = []
        for key in mem.keys():
            results.append(mem[key])
        return results
