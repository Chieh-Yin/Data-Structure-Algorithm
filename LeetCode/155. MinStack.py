class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        
        self.list = []
        self.size = 0

    def push(self, x: int) -> None:
        
        self.list.append(x)
        self.size+= 1    
      
    def pop(self) -> None:
        
        if self.size == 0:
            return
        else:
            self.list.pop(self.size-1)
            self.size-= 1

    def top(self) -> int:
        
        return self.list[self.size-1]

    def getMin(self) -> int:
        
        return min(self.list)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
