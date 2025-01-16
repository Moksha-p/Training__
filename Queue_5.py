from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

lru = LRUCache(3)
lru.put(1, 1)
lru.put(2, 2)
lru.put(3, 3)
print(lru.get(2)) 
lru.put(4, 4)
print(lru.get(1)) 