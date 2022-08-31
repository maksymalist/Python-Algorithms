class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.storage = {}
        self.queue = []
        

    def get(self, key: int) -> int:
        if key in self.storage:
            i = self.queue.index(key)
            self.queue.append(self.queue.pop(i))
            return self.storage[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.storage:
            self.queue.pop(self.queue.index(key))
            self.queue.append(key)
            self.storage[key] = value
            
            print(self.storage)
            print(self.queue)
            return
        
        if  len(self.storage.keys()) >= self.capacity:
            lru = self.queue.pop(0)
            self.storage.pop(lru)
            
        self.queue.append(key)
        self.storage[key] = value
        
        print(self.storage)
        print(self.queue)