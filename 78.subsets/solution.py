class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        []
        -------
        [] + [1] => [1]
        -------
        [] + [2] => [2]
        [1] + [2] => [1, 2]
        -------
        [] + [3] => [3]
        [1] + [3] => [1, 3]
        [2] + [3] => [2, 3]
        [1, 2] + [3] => [1, 2, 3]
        """
        results = [
            []
        ]
        for num in nums:
            for i in range(len(results)):
                results.append(results[i] + [num])
        return results
