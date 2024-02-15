class OrderedStream:
    def __init__(self, n: int):
        self.n = n
        self.chunks = [None]*n
        self.ptr = 0
        
    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -= 1
        self.chunks[idKey] = value
        
        if idKey > self.ptr:
            return []
        
        while self.ptr < len(self.chunks) and self.chunks[self.ptr]:
            self.ptr += 1

        return self.chunks[idKey:self.ptr]
 
# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)