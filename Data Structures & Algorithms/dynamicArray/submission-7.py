class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.size: int = 0
        self.index_to_value: dict[int, int] = {}

    def get(self, i: int) -> int:
        return self.index_to_value[i]

    def set(self, i: int, n: int) -> None:
        if i < self.capacity:
            if i not in self.index_to_value :
                self.size += 1
            self.index_to_value[i] = n


    def pushback(self, n: int) -> None:
        if self.size + 1 > self.capacity :
            self.resize()
        self.index_to_value[self.size] = n
        self.size += 1

    def popback(self) -> int:
        val = self.index_to_value[self.size - 1]
        self.size -= 1
        return val

    def resize(self) -> None:
        self.capacity *= 2 

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
