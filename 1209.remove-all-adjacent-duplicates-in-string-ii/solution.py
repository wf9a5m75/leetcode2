class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack1 = [""]
        stack2 = [0]
        for c in s:
            if stack1[-1] == c:
                stack2[-1] += 1
                stack1.append(c)
                if (stack2[-1] == k):
                    while(stack2[-1] > 0):
                        stack1.pop()
                        stack2[-1] -= 1
                    stack2.pop()
            else:
                stack1.append(c)
                stack2.append(1)
        return "".join(stack1)
