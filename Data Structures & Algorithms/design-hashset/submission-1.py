class MyHashSet:

    def __init__(self):
        self.size = 10000
        self.hash_set = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        idx = self._hash(key)

        if key not in self.hash_set[idx]:
            self.hash_set[idx].append(key)

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        if key in self.hash_set[idx]:
            self.hash_set[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        if key in self.hash_set[idx]:
            return True

        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)