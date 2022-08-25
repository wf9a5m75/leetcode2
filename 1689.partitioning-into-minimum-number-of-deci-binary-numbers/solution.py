class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        counts = Counter(operations)
        return counts.get("++X", 0)  + counts.get("X++", 0) - counts.get("--X",0) - counts.get("X--",0)
