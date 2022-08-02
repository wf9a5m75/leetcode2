class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        keys = sorted(list(freq.keys()), key = lambda char: -freq[char])
        buffer = ""
        for char in keys:
            buffer += char * freq[char]
        return buffer
        
