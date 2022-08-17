class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        if (len(words) < 2):
            return len(words)
        patterns = set()
        table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."];

        for word in words:
            result = ""
            for char in word:
                result += table[ord(char) - 97]
            patterns.add(result)
        return len(patterns)
