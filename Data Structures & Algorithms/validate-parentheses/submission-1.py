class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for c in s:
            if c in pairs.keys():
                if len(stack) == 0 or stack.pop() != pairs[c]:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0

        