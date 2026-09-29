class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, val: int) -> None:
        self.stack.insert(0, val)
        if(len(self.min_stack) <= 0 or self.min_stack[0] >= val):
            self.min_stack.insert(0, val)

    def pop(self) -> None:
        temp = self.stack[0]
        del self.stack[0]
        if(len(self.min_stack) > 0 and self.min_stack[0] == temp):
            del self.min_stack[0]

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        return self.min_stack[0]

        
