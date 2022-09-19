import re
class Solution:
    def getHashCode(self, contents: str) -> int:
        # https://stackoverflow.com/a/15518635/697856

        result = 0
        multiplier = 1
        N = len(contents)
        for i in range(N):
            result += ord(contents[i]) * multiplier
            shifted = multiplier << 5
            multiplier = shifted - multiplier
        return result

    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        groups = {}
        dirPaths = {}

        for path in paths:
            tmp = path.split()
            dirPath = tmp.pop(0)
            files = tmp

            for file in files:
                tmp = re.split("[\(\)]", file)
                filename, contents = tmp[0], tmp[1]
                contentsHash = self.getHashCode(contents)

                files2 = groups.get(contentsHash, [])
                files2.append(f"{dirPath}/{filename}")
                groups[contentsHash] = files2

        results = []
        for contentsHash in groups.keys():

            files = groups[contentsHash]
            if (len(files) > 1):
                results.append(files)

        return results
