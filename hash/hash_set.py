class MyHashSet:
    def __init__(self):
        self.num_of_buckets = 10000
        self.buckets = [[] for i in range(self.num_of_buckets)]

    def _hash_func(self, key: int) -> int:
        return key % self.num_of_buckets

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.buckets[self._hash_func(key)].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.buckets[self._hash_func(key)].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.buckets[self._hash_func(key)]