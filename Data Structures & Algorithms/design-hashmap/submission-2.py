class Node:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.next = None

class MyHashMap:
    def __init__(self):
        self.limit = 10000
        self.hash_map = [Node(0, 0) for _ in range(self.limit)]

    def get_index_from_key(self, key: int) -> int:
        return key % self.limit


    def put(self, key: int, value: int) -> None:
        index = self.get_index_from_key(key)

        if self.hash_map[index].next is not None:
            head = self.hash_map[index].next
            while head.next is not None and head.key != key:
                head = head.next
            head.val = value

        else:
            new_node = Node(value, key)
            self.hash_map[index].next = new_node

    def get(self, key: int) -> int:
        index = self.get_index_from_key(key)
        if self.hash_map[index].next is None: return -1
        else:
            head = self.hash_map[index].next
            while head.next is not None and head.key != key:
                head = head.next

            return head.val

    def remove(self, key: int) -> None:
        index = self.get_index_from_key(key)
        if self.hash_map[index].next is not None:
            self.hash_map[index].next = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)