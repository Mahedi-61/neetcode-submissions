class MyHashSet:
    def __init__(self):
        self.array = [[] for _ in range(10_000)]
        

    def add(self, key: int) -> None:
        idx = key % 10_000
        idx_array = self.array[idx]
        
        if key not in idx_array:
            idx_array.append(key)
        

    def remove(self, key: int) -> None:
        idx = key % 10_000
        idx_array = self.array[idx]

        if key in idx_array:
            idx_array.remove(key)


    def contains(self, key: int) -> bool:
        idx = key % 10_000
        idx_array = self.array[idx]

        if key in idx_array:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)