class MyHashMap:
    def __init__(self):
        self.hash_map = [[] for _ in range(10_000)]
        self.hash_val = [[] for _ in range(10_000)]

    def hashf(self, key):
        return key % 10_000

    def put(self, key: int, value: int) -> None:
        idx = self.hashf(key)
        if key in self.hash_map[idx]:
            key_idx = self.hash_map[idx].index(key)
            self.hash_val[idx][key_idx] = value
        else:
            self.hash_map[idx].append(key)
            self.hash_val[idx].append(value)

    def get(self, key: int) -> int:
        idx = self.hashf(key)
        if key in self.hash_map[idx]:
            key_idx = self.hash_map[idx].index(key)
            return self.hash_val[idx][key_idx]

        return -1

    def remove(self, key: int) -> None:
        idx = self.hashf(key)

        if key in self.hash_map[idx]:
            key_idx = self.hash_map[idx].index(key)
            del self.hash_map[idx][key_idx]
            del self.hash_val[idx][key_idx]

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)