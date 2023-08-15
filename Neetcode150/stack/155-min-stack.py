class MinStack:

    def __init__(self):
        self.stack = [] # (value, min_value when pushing)
        self.min = float('inf')

    def push(self, val: int) -> None:
        self.stack.append((val, self.min))
        if val < self.min:
            self.min = val

    def pop(self) -> None:
        top = self.stack.pop()
        if top[0] == self.min:
            self.min = top[1] # update min value to be equal to the next smallest
        return top[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()