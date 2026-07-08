from collections import deque
class MinStack:
    
    def __init__(self):
        self.stack = deque()
        self.mini = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return min(self.stack)
        
