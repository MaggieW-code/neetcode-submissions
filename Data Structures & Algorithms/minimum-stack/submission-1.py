class MinStack:

    def __init__(self):
        self.item = []
        self.minv = []

    def push(self, val: int) -> None:
        self.item.append(val)
        if not self.minv:
            self.minv.append(val)
        else:
            self.minv.append(min(self.minv[-1],val))

    def pop(self) -> None:
        if not self.item:
            return None
        self.minv.pop()
        return self.item.pop()

    def top(self) -> int:
        if not self.item:
            return None
        return self.item[-1]

    def getMin(self) -> int:
        if not self.minv:
            return None
        return self.minv[-1]