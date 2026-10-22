class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.capacity_used = 0
        self.cache = {}
        self.removal_queue = list()

    def __str__(self) :
        return f"""Capcity : {self.capacity} ; 
                   Capcity_used : {self.capacity_used} ; 
                   Cache : {self.cache} ;
                   Removal Queue : {self.removal_queue} ;"""

    def get(self, key: int) -> int:
        val = self.cache.get(key, -1)
        if val != -1 :
            self._update_removal_queue(key)
        print(f"GET : ", val, str(self))
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache :
            self.cache[key] = value
        else :
            if self.capacity_used < self.capacity :
                self.cache[key] = value
                self.capacity_used += 1 
            else :
                del self.cache[self._get_key_to_remove()]
                self.cache[key] = value
            self.removal_queue.append(key)
        print(f"PUT : ", value, str(self))
        self._update_removal_queue(key)
    
    def _update_removal_queue(self, key:int) -> None :
        self.removal_queue.remove(key)
        self.removal_queue.append(key)

    def _get_key_to_remove(self) -> int :
        key = self.removal_queue[0]
        self.removal_queue.remove(key)
        return key
