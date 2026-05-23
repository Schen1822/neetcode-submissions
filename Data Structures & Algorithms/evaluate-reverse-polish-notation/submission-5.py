import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": lambda x,y: int(x) + int(y),
            "-": lambda x, y: int(x) - int(y),
            "*": lambda x, y: int(x) * int(y),
            "/": lambda x, y: math.trunc(int(x)/int(y)),
        }
        stack = []
        for c in tokens:
            if not (c in ops):
                stack.append(int(c))
            else:
                y = stack.pop()
                x = stack.pop()
                res = ops[c](x, y)
                print(x, c, y, res)
                stack.append(res)
        return stack.pop()
        