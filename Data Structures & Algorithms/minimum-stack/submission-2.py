import heapq

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_ = None

    def push(self, val: int) -> None:
        if len(self.stack) == 0 :
            self.stack.append(0)
            self.min_ = val
        else :
            self.stack.append(val - self.min_)
            if val - self.min_ < 0 :
                self.min_ = val


    def pop(self) -> None:
        poped_val = self.stack.pop()
        if poped_val < 0 :
            self.min_ -= poped_val

    def top(self) -> int:
        if self.stack[-1] < 0 :
            return self.min_
        else :
            return self.stack[-1] + self.min_

    def getMin(self) -> int:
        return self.min_
