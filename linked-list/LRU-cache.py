class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache.pop(key)
            self.cache[key] = val
            return val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        elif len(self.cache.keys()) == self.capacity:
            del self.cache[list(self.cache.keys())[0]]
            self.cache[key] = value
        else:
            self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)