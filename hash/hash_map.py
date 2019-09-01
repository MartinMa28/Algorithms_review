class MyHashMap:
    def __init__(self):
        self.num_of_buckets = 7919
        self.buckets = [[] for _ in range(self.num_of_buckets)]

    
    def _hash_func(self, key):
        return key % self.num_of_buckets


    def put(self, key: int, value: int) -> None:
        prev_val = self.get(key)
        if prev_val < 0:
            self.buckets[self._hash_func(key)].append((key, value))
        else:
            self.buckets[self._hash_func(key)].remove((key, prev_val))
            self.buckets[self._hash_func(key)].append((key, value))

    
    def get(self, key: int) -> int:
        for k, val in self.buckets[self._hash_func(key)]:
            if k == key:
                return val

        return -1
         
        
    def remove(self, key: int) -> None:
        for k, val in self.buckets[self._hash_func(key)]:
            if k == key:
                self.buckets[self._hash_func(key)].remove((k, val))
                break
