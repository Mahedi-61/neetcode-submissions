class Node:
    def __init__(self, val=-1, key=-1, next=None):
        self.val = val
        self.key = key
        self.next = next

class MyHashMap:
    def __init__(self):
        self.limit = 10000
        self.hash_map = [Node() for _ in range(self.limit)]

    def get_hash(self, key: int) -> int:
        return key % self.limit

    def put(self, key: int, value: int) -> None:
        index = self.get_hash(key)
        head = self.hash_map[index]

        while head.next:
            if head.next.key == key:
                head.next.val = value
                return
            head = head.next

        new_node = Node(value, key)
        head.next = new_node


    def get(self, key: int) -> int:
        index = self.get_hash(key)
        head = self.hash_map[index].next

        while head:
            if head.key == key:
                return head.val
            head = head.next
        return -1

    def remove(self, key: int) -> None:
        index = self.get_hash(key)
        if self.hash_map[index].next is not None:
            self.hash_map[index].next = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)