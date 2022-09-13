class Solution:
    def validUtf8(self, data: List[int]) -> bool:

        size = len(data)
        i = 0
        cnt = 0
        while(i < size):
            if (cnt > 0):
                # data[i] should be 0b10xxxxxx
                if (data[i] & 0xC0) != 0x80:
                    return False
                cnt -= 1
                i += 1
                continue


            if (data[i] & 0x80) == 0:
                # 1 byte character
                cnt = 0
            elif (data[i] & 0xE0) == 0xC0:
                # 2 byte character
                cnt = 1
            elif (data[i] & 0xF0) == 0xE0:
                # 3 byte character
                cnt = 2
            elif (data[i] & 0xF8) == 0xF0:
                # 4 byte character
                cnt = 3
            else:
                return False
            i += 1
        return (cnt == 0)
