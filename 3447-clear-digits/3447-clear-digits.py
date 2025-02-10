class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for n in s:
            if n.isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(n)
        return "".join(stack)