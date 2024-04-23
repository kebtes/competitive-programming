# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current_size = 0
        self.cache_mapping = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache_mapping:
            return -1

        self.cache_mapping.move_to_end(key)
        return self.cache_mapping[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache_mapping:
            self.cache_mapping[key] = value
            self.cache_mapping.move_to_end(key)
            return 
        
        if self.current_size >= self.capacity:
            cache_key = next(iter(self.cache_mapping))
            del self.cache_mapping[cache_key]
            
        else:
            self.current_size += 1
        
        self.cache_mapping[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)