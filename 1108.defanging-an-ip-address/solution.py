import re
class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = re.sub("\.","[.]", address)
        return address
