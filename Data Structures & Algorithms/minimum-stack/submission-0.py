class MinStack:

    def __init__(self):
        self.stack = []
        self.minIndex = -1
        

    def push(self, val: int) -> None:
        if self.minIndex == -1:
            self.stack.append({"value": val, "pointer": -1})
            self.minIndex = len(self.stack)-1
        elif self.stack[self.minIndex]["value"] > val:
            self.stack.append({"value": val, "pointer": self.minIndex})
            self.minIndex = len(self.stack) - 1
        else:
            self.stack.append({"value": val, "pointer": -1})
        

    def pop(self) -> None:
        if self.minIndex == len(self.stack) - 1:
            popped = self.stack.pop()
            self.minIndex = popped["pointer"]
        else: 
            self.stack.pop()
        

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]["value"]
        

    def getMin(self) -> int:
        return self.stack[self.minIndex]["value"]
        
