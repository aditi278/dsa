       
class MinStack:

    def __init__(self):
        self.stack = []
        self.length = 0

    def push(self, val: int) -> None:
        if self.length:
            self.stack.append([val, min(val, self.getMin())])
        else:
            self.stack.append([val, val])
        self.length +=1
            

    def pop(self) -> None:
        self.stack.pop()
        self.length-=1

    def top(self) -> int:
        return self.stack[self.length-1][0]

    def getMin(self) -> int:
        return self.stack[self.length-1][1]