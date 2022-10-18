class Solution:
    def compress(self, chars: List[str]) -> int:
        cnt = 0
        prev = chars[0]
        chars.append("")

        i = 0
        for c in chars:
            if prev == c:
                cnt += 1
            else:
                if cnt == 1:
                    chars[i] = prev
                    i += 1
                else:
                    tmp = str(cnt)
                    chars[i] = prev
                    i += 1

                    for d in tmp:
                        chars[i] = d
                        i += 1
                cnt = 1
                prev = c
        return i
